# 🛡️ PhishDetect

> A modern phishing URL detection tool powered by the VirusTotal API.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📖 About

PhishDetect is an open-source command-line tool that scans URLs using the VirusTotal API.

It helps users quickly inspect suspicious links by displaying a clean summary of security detections and detailed vendor analysis in a modern terminal interface.

---

## ✨ Features

- 🔍 Scan a single URL
- 🛡️ VirusTotal URL analysis
- 📊 Rich terminal interface
- 📋 Security vendor results
- 💾 Automatic report generation
- 🔑 Secure local API key storage
- 📁 Batch scan support (Coming Soon)
- 🌍 IP & WHOIS Lookup (Planned)
- 🚀 Cross-platform (Linux & Termux)

---

## 📷 Preview

```text
╭───────────────────────────────╮
│         PhishDetect           │
╰───────────────────────────────╯

✔ Configuration Loaded
✔ API Loaded

┌──────── Scan Summary ────────┐
│ Malicious      : 0           │
│ Suspicious     : 0           │
│ Harmless       : 61          │
│ Undetected     : 31          │
└──────────────────────────────┘
```

---

## 📂 Project Structure

```
PhishDetect/
│
├── banner.py
├── config.py
├── scanner.py
├── utils.py
├── menu.py
├── main.py
│
├── config/
│   └── config.json
│
├── reports/
│
├── README.md
├── LICENSE
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Devillboygamerz/PhishDetect.git
```

Enter the directory

```bash
cd PhishDetect
```

Install requirements

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

## 🔑 VirusTotal API

Create a free account on VirusTotal and generate your API key.

The first time you run PhishDetect, you'll be prompted to enter your API key. It will be stored locally in:

```
config/config.json
```

Your API key is **never included in this repository**.

---

## 📋 Roadmap

- [x] VirusTotal API
- [x] Rich Terminal UI
- [x] Report Generation
- [ ] Batch URL Scanning
- [ ] WHOIS Lookup
- [ ] IP Geolocation
- [ ] DNS Lookup
- [ ] SSL Certificate Information
- [ ] URLScan Integration

---

## ⚠️ Disclaimer

This project is intended for **educational, research, and defensive cybersecurity purposes only**.

Always ensure you have authorization before analyzing systems or websites in environments where permission is required.

The author is not responsible for misuse of this software.

---

## 👨‍💻 Author

**Inshad Ameer**

GitHub:
https://github.com/Devillboygamerz

Instagram:
@_ameer_734

if you reading this I will give my api key coz I don't use it

989573c0ff4c57f2f3516cd93674dd748b88c89f9fb7429a41c94fc0791a10e5

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

---

Made with ❤️, Python and ☕