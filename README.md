Detect Scam Emails & Malicious URLs using Flask + AI

A cybersecurity web application that detects:

Scam/Fake emails and messages
Malicious or phishing URLs

Built using:

Python
Flask
HTML/CSS
AI-inspired phishing detection logic
Features
Detect phishing/scam URLs
Analyze uploaded TXT and PDF files
Scam email/message detection
User-friendly web interface
Real-time detection results
Cybersecurity-focused project
Tech Stack
Python
Flask
HTML
CSS
PyPDF2
VS Code
Project Structure
project-folder/
│
├── templates/
│ └── index.html
│
├── main.py
├── requirements.txt
├── README.md
└── venv/
Installation

1. Clone Repository
   git clone https://github.com/your-username/scam-detection-app.git
2. Open Project
   cd scam-detection-app
3. Create Virtual Environment
   Windows
   python -m venv venv

Activate:

venv\Scripts\activate 4. Install Dependencies
pip install flask PyPDF2
Run the Project
python main.py

Example malicious URL:

http://secure-paypal-login-free.xyz

Example safe URL:

https://google.com
File Detection

Supported file types:

.txt
.pdf

The application analyzes uploaded files and detects scam/phishing content.

Detection Logic

The application checks for:

Suspicious phishing keywords
Fake login indicators
Dangerous domains
Scam-related patterns
Fraudulent email phrases

Future Improvements
Machine Learning based detection
VirusTotal API integration
Gemini/OpenAI AI integration
Dark mode UI
Login system
Detection history database
Real-time threat intelligence
Educational Purpose

This project is developed for:

Cybersecurity learning
College projects
Resume building
Internship showcase

Author
Sonali Jain
Computer Science Student | Cybersecurity Enthusiast
