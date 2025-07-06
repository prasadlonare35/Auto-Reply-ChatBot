# 🤖 AutoRoastBot

An AI-powered Python bot that **automatically reads WhatsApp chat messages from screen, generates savage roast replies using Google Gemini AI**, and auto-sends them back — just for fun! 🔥😎

![Demo](demo.gif)

---

## ✨ Features
- 📋 Reads messages from WhatsApp Web screen
- ⚡ Generates short, witty roast replies in English or According to given context
- 🧠 Uses Google Gemini AI (gemini-2.0-flash)
- ⌨️ Auto-pastes and sends replies via pyautogui
- 🖱️ Captures screen coordinates dynamically (using helper script)

---

## 🛠 Tech Stack
- Python
- Google Gemini API
- pyautogui
- pyperclip
- dotenv

---

## 📦 Installation

1.Clone this repo:
   
      git clone https://github.com/prasadlonare35/AutoRoastBot.git
      cd AutoRoastBot
   
2.Install dependencies:

      pip install -r requirements.txt
      
3.Configure your API key:
Create a .env file:

    GEMINI_API_KEY=your_gemini_api_key
    
▶️ Usage
Open WhatsApp Web and adjust your window so the bot can read the messages.

4.(Optional) Use get_cursor.py to find screen coordinates if your resolution differs.

5.Run the bot:

    python main.py

✅ The bot will copy chat history, ask Gemini AI for a roast reply, then auto-paste & send it.

⚠️ Disclaimer
This project is for educational and fun purposes only.
Please use responsibly and do not spam or harass others.

🚀 Made with Python, coffee ☕, and lots of 🤖 by Prasad
