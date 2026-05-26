from flask import Flask, render_template, request
import os
import PyPDF2

app = Flask(__name__)

# --------------------------------
# Scam Text Detection
# --------------------------------
def predict_fake_or_real_email_content(text):

    text = text.lower()

    scam_keywords = [
        "urgent",
        "winner",
        "lottery",
        "free money",
        "bank account",
        "click here",
        "verify account",
        "password",
        "credit card",
        "otp",
        "claim reward",
        "limited time"
    ]

    score = 0

    for word in scam_keywords:
        if word in text:
            score += 1

    if score >= 2:
        return "⚠ Scam/Fake Message Detected"
    else:
        return "✅ Legitimate Message"


# --------------------------------
# URL Detection
# --------------------------------
def url_detection(url):

    url = url.lower()

    phishing_keywords = [
        "login",
        "verify",
        "secure",
        "update",
        "paypal",
        "bank",
        "free",
        "bonus",
        "gift"
    ]

    suspicious_domains = [
        ".xyz",
        ".tk",
        ".ru",
        ".top"
    ]

    score = 0

    for word in phishing_keywords:
        if word in url:
            score += 1

    for domain in suspicious_domains:
        if domain in url:
            score += 1

    if score >= 3:
        return "phishing"

    elif score == 2:
        return "malware"

    else:
        return "benign"


# --------------------------------
# Home Route
# --------------------------------
@app.route('/')
def home():
    return render_template("index.html")


# --------------------------------
# Scam File Detection
# --------------------------------
@app.route('/scam/', methods=['POST'])
def detect_scam():

    if 'file' not in request.files:
        return render_template(
            "index.html",
            message="No file uploaded."
        )

    file = request.files['file']

    extracted_text = ""

    if file.filename.endswith('.pdf'):

        pdf_reader = PyPDF2.PdfReader(file)

        extracted_text = " ".join(
            [
                page.extract_text()
                for page in pdf_reader.pages
                if page.extract_text()
            ]
        )

    elif file.filename.endswith('.txt'):

        extracted_text = file.read().decode("utf-8")

    else:
        return render_template(
            "index.html",
            message="Upload PDF or TXT only."
        )

    if not extracted_text.strip():
        return render_template(
            "index.html",
            message="Could not extract text."
        )

    message = predict_fake_or_real_email_content(extracted_text)

    return render_template(
        "index.html",
        message=message
    )


# --------------------------------
# URL Detection Route
# --------------------------------
@app.route('/predict', methods=['POST'])
def predict_url():

    url = request.form.get('url', '').strip()

    if not url.startswith(("http://", "https://")):

        return render_template(
            "index.html",
            message="Invalid URL format.",
            input_url=url
        )

    classification = url_detection(url)

    return render_template(
        "index.html",
        input_url=url,
        predicted_class=classification
    )


# --------------------------------
# Run App
# --------------------------------
if __name__ == '__main__':
    app.run(debug=True)