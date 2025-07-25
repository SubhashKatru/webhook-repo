# Webhook Receiver for GitHub Events

# Webhook Receiver for GitHub Events – TechStaX Assignment

This project is built using **Flask + MongoDB** to receive and display GitHub webhook events in real time.

## 🔧 Features
- Receives GitHub events: Push, Pull Request, Merge
- Stores events in MongoDB
- Shows events on a simple HTML UI
- Auto-refreshes every 15 seconds

## 💻 Technologies
- Python + Flask
- MongoDB
- HTML + JavaScript (Polling)
- Ngrok (for tunneling)

## 🔗 Related Repo

This repo receives webhooks from a dummy GitHub repo:  
👉 [`action-repo`](https://github.com/SubhashKatru/action-repo)

## 🚀 How to Run Locally

1. Clone the repo:
git clone https://github.com/SubhashKatru/webhook-repo.git
cd webhook-repo

2. Install dependencies:
pip install -r requirements.txt

3. Run MongoDB (locally or via Atlas)

4. Start Flask:
python app.py

5. Start ngrok:
ngrok http 5000

6. Add the ngrok URL to GitHub Webhook settings.

## 📄 Submission Details

Submitted for: TechStaX Full-Time Developer Role  
Due Date: July 6, 2025  
Submitted on: ✅ July 5, 2025

---