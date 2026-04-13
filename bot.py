import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from database import init_db, subscribe_user, unsubscribe_user, get_all_subscribers
from quotes import get_next_quote, get_random_quote

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

async def send_scheduled_motivation(context: ContextTypes.DEFAULT_TYPE):
    message = get_next_quote()
    subs = get_all_subscribers()
    
    for user_id in subs:
        try:
            await context.bot.send_message(chat_id=user_id, text=message, parse_mode='Markdown')
        except Exception as e:
            logging.error(f"Could not send to {user_id}: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome = (
        "Welcome to **MotivaCoreBot**! 💡\n\n"
        "I deliver powerful motivational messages every 3 hours to keep you on track.\n\n"
        "Commands:\n"
        "/subscribe - Opt-in for 3-hourly messages\n"
        "/unsubscribe - Stop receiving messages\n"
        "/motivate - Get a message instantly"
    )
    await update.message.reply_text(welcome, parse_mode='Markdown')

async def motivate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_random_quote(), parse_mode='Markdown')

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if subscribe_user(update.effective_user.id):
        await update.message.reply_text("✅ Success! You are now subscribed to receive motivation every 3 hours.")
    else:
        await update.message.reply_text("You are already on the list! 🚀")

async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if unsubscribe_user(update.effective_user.id):
        await update.message.reply_text("❌ You have unsubscribed. Stay strong on your journey!")
    else:
        await update.message.reply_text("You aren't currently subscribed.")

def main():
    init_db()
    app = ApplicationBuilder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("motivate", motivate))
    app.add_handler(CommandHandler("subscribe", subscribe))
    app.add_handler(CommandHandler("unsubscribe", unsubscribe))

    # Scheduler: Every 3 hours (10800 seconds)
    job_queue = app.job_queue
    job_queue.run_repeating(send_scheduled_motivation, interval=10800, first=10)

    logging.info("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
