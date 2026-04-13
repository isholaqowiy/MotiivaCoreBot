# 💡 MotivaCoreBot

MotivaCoreBot is a professional Telegram bot built with `python-telegram-bot` v20+. It is designed to help users stay inspired by delivering high-quality motivational quotes and mindset tips every 3 hours, 24/7.

## 🚀 Features
- **Automated Delivery**: Sends motivation every 3 hours to all subscribers.
- **On-Demand Motivation**: Use `/motivate` to get an instant boost.
- **Subscriber Management**: Simple `/subscribe` and `/unsubscribe` commands.
- **Variety Guaranteed**: Uses a rotation logic to ensure quotes don't repeat too often.
- **Persistent Storage**: Uses SQLite to keep track of subscribers even after restarts.

## 🛠 Tech Stack
- **Language**: Python 3.12+
- **Library**: [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) (v20.x)
- **Scheduler**: APScheduler (integrated into the library's JobQueue)
- **Database**: SQLite3
- **Deployment**: Optimized for Render Background Workers

## 📦 Project Structure
- `bot.py`: Main entry point containing command handlers and the automation loop.
- `database.py`: Handles all SQLite interactions (subscriptions and state tracking).
- `quotes.py`: Contains the motivational content and selection logic.
- `requirements.txt`: List of Python dependencies.

---

## 🏗 Deployment on Render.com

Since this bot uses "Polling" and runs scheduled tasks, it is best deployed as a **Background Worker**.

### Step 1: Prepare your Bot
1. Create a bot and get your **API Token** from [@BotFather](https://t.me/botfather) on Telegram.
2. Push this project code to a GitHub repository.

### Step 2: Create a Render Background Worker
1. Log in to [Render](https://render.com).
2. Click **New +** and select **Background Worker**.
3. Connect your GitHub repository.
4. Configure the following settings:
   - **Name**: `motivacore-bot`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`

### Step 3: Configure Environment Variables
Navigate to the **Environment** tab in your Render service and add the following:

| Key | Value |
| :--- | :--- |
| `BOT_TOKEN` | *Your Telegram Bot Token* |
| `PYTHON_VERSION` | `3.12.2` |

### Step 4: Deploy
Click **Create Background Worker**. Once the build is finished, check the logs. You should see `Bot started...` and the bot will begin its 3-hour cycle immediately.

---

## 🤖 Bot Commands
- `/start` - Welcome message and instructions.
- `/subscribe` - Join the list for 3-hourly motivation.
- `/unsubscribe` - Stop receiving automated messages.
- `/motivate` - Receive an instant motivational quote.

## ⚠️ Important Note on Storage
Render's free tier Background Workers use an **ephemeral file system**. This means the `motiva.db` file (SQLite) will reset whenever the bot is redeployed or restarted. For permanent data storage, consider connecting the bot to an external PostgreSQL database.

## 📜 License
This project is open-source and available under the MIT License.
