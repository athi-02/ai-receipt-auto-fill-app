# AI Receipt Auto-Fill App

An AI-powered Flask web application that extracts receipt information automatically using Google Gemini AI.

Users can upload a receipt image, review the extracted information, edit it if needed, and save the receipt into a local history dashboard.

---

# Features

- AI receipt data extraction using Gemini AI
- Upload receipt image
- Automatic extraction of:
  - Merchant Name
  - Date
  - Total Amount
  - Currency
- Editable review form before submission
- Receipt image preview
- Dark mode / Light mode
- Loading spinner during AI processing
- Receipt history dashboard
- Delete receipt records
- CSV export support
- Local JSON data storage
- Modern responsive UI

---

# Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Google Gemini API

---

# Project Structure

```bash
receipt-autofill-app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── receipts.json
│   └── receipts_export.csv
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
└── templates/
    ├── index.html
    ├── result.html
    ├── success.html
    └── history.html
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/athi-02/ai-receipt-auto-fill-app.git
```

## 2. Navigate into Project Folder

```bash
cd ai-receipt-auto-fill-app
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=AIzaSyCFs-CquQsxEZLyfSSNKa_6Cb90YdGWt-c
```

---

# Run the Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Future Improvements

- Cloud database integration
- OCR enhancement
- User authentication
- Receipt categorization
- Analytics dashboard
- Online deployment

---

# Author

Developed by ATHIYAMAH A/P BALA KRISHNAN
