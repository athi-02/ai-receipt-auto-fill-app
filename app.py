from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import os
import json
import csv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():

    receipt = request.files['receipt']

    if not receipt:
        return "No file uploaded"

    # Save uploaded image
    filepath = os.path.join(UPLOAD_FOLDER, receipt.filename)
    receipt.save(filepath)

    # Open image for Gemini
    image = Image.open(filepath)

    prompt = """
    Extract the following information from this receipt image:

    - merchant_name
    - date
    - total_amount
    - currency

    Return ONLY valid JSON.

    Example:
    {
      "merchant_name": "KFC",
      "date": "2026-05-10",
      "total_amount": "25.90",
      "currency": "MYR"
    }
    """

    response = model.generate_content([prompt, image])

    raw_text = response.text.strip()
    raw_text = raw_text.replace("```json", "").replace("```", "")

    try:
        data = json.loads(raw_text)

    except:
        return f"""
        <h2>AI Response Error ❌</h2>
        <pre>{raw_text}</pre>
        """

    return render_template(
        "result.html",
        merchant_name=data.get("merchant_name", ""),
        date=data.get("date", ""),
        total_amount=data.get("total_amount", ""),
        currency=data.get("currency", ""),
        receipt_image=filepath
    )


@app.route('/submit', methods=['POST'])
def submit():

    merchant_name = request.form.get("merchant_name")
    date = request.form.get("date")
    total_amount = request.form.get("total_amount")
    currency = request.form.get("currency")

    receipt_data = {
        "merchant_name": merchant_name,
        "date": date,
        "total_amount": total_amount,
        "currency": currency
    }

    # Read existing data
    with open("data/receipts.json", "r") as file:
        receipts = json.load(file)

    # Add new receipt
    receipts.append(receipt_data)

    # Save updated data
    with open("data/receipts.json", "w") as file:
        json.dump(receipts, file, indent=4)

    return render_template(
        "success.html",
        merchant_name=merchant_name,
        date=date,
        total_amount=total_amount,
        currency=currency
    )

@app.route('/history')
def history():

    with open("data/receipts.json", "r") as file:
        receipts = json.load(file)

    receipts.reverse()

    total_receipts = len(receipts)

    total_spending = 0

    for receipt in receipts:
        try:
            total_spending += float(receipt["total_amount"])
        except:
            pass

    latest_merchant = receipts[0]["merchant_name"] if receipts else "N/A"

    return render_template(
        "history.html",
        receipts=receipts,
        total_receipts=total_receipts,
        total_spending=round(total_spending, 2),
        latest_merchant=latest_merchant
    )

@app.route('/export')
def export():

    with open("data/receipts.json", "r") as file:
        receipts = json.load(file)

    csv_file_path = "data/receipts_export.csv"

    with open(csv_file_path, mode="w", newline="") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "Merchant Name",
            "Date",
            "Total Amount",
            "Currency"
        ])

        for receipt in receipts:

            writer.writerow([
                receipt["merchant_name"],
                receipt["date"],
                receipt["total_amount"],
                receipt["currency"]
            ])

    return send_file(
        csv_file_path,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)