# 🤖 PersonalBoat - AI Chatbot for Discord

A Discord chatbot built using Python, Discord API, and OpenAI GPT-4o. The bot listens to messages in Discord and responds with AI-generated text using OpenAI's GPT model.

---

## 🚀 Features
- ✅ AI-Powered Responses – Uses GPT-4o for smart and natural replies.
- ✅ Discord Integration – Works in any Discord server.
- ✅ Handles Long Messages – Automatically splits responses over 2000 characters.
- ✅ Secure API Key Management – Uses `.env` file to store sensitive tokens.
- ✅ Customizable AI Personality – Modify the bot’s response style.

---

## 📌 Technologies Used

| Technology  | Purpose                             |
|-------------|-------------------------------------|
| Python      | Core programming language           |
| Discord API | For bot integration with Discord    |
| OpenAI API  | Generates AI responses using GPT-4o |
| dotenv      | Loads environment variables securely|

---

## 🛠 Installation & Setup

1️⃣ Clone the Repository
bash
git clone https://github.com/RihilSanghani/PersonalBoat.git
cd PersonalBoat

2️⃣ Install Dependencies
Make sure you have Python 3.8+ installed, then run:
pip install -r requirements.txt
(If requirements.txt is not available, install manually: pip install discord openai python-dotenv.)

3️⃣ Create a .env File
Inside the project folder, create a .env file to store API keys:
touch .env
Then, add the following (replace with your actual keys):
DISCORD_TOKEN=your_discord_bot_token
OPEN_AI_API_KEY=your_openai_api_key

4️⃣ Run the Bot
python bot.py
