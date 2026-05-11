# AI Receipt Auto-Fill Web App

An AI-powered receipt processing web application built with Flask and Google Gemini AI.

This application allows users to upload receipt images, automatically extract important receipt information using generative AI, review/edit the extracted data, and manage receipt history through a clean dashboard interface.

---

# Features

- Upload receipt images
- AI-powered receipt information extraction
- Editable auto-filled form
- Receipt image preview
- Loading spinner during AI processing
- Local JSON-based receipt storage
- Receipt history dashboard
- Analytics cards
- CSV export functionality
- Modern responsive UI using Bootstrap 5

---

# Technologies Used

- Python
- Flask
- Google Gemini AI API
- HTML5
- Bootstrap 5
- JSON
- JavaScript

---

# Extracted Receipt Fields

The application extracts:

- Merchant Name
- Date
- Total Amount
- Currency

---

# Project Structure

```bash
receipt-autofill-app/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   └── receipts.json
│
├── static/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── success.html
│   └── history.html
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-github-repo-url>
cd receipt-autofill-app
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 5. Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# AI Model Used

- Google Gemini 2.5 Flash

Prompting was used to extract structured JSON receipt information from uploaded receipt images.

---

# Future Improvements

- Database integration
- User authentication
- Multi-currency analytics
- OCR confidence scoring
- Cloud deployment

---

# Author

Developed by ATHIYAMAH A/P BALA KRISHNAN