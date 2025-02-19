from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import asyncio

TOKEN = "8007060492:AAFNr28xUM6QnX4w6AIRrj2Um43ZpEa_5ZU"
WEBHOOK_URL = "https://yourdomain.com/webhook"  # अपने सर्वर का URL डालें

app = Flask(__name__)

# Telegram Bot Application
bot_app = Application.builder().token(TOKEN).build()

# /start कमांड का फंक्शन
async def start(update: Update, context: CallbackContext):
    image_url = "https://envs.sh/Q0_.jpg"
    keyboard = [
        [InlineKeyboardButton("🔽 Download 1", url="https://example.com/download1"),
         InlineKeyboardButton("🔽 Download 2", url="https://example.com/download2")],
        [InlineKeyboardButton("🔽 Download 3", url="https://example.com/download3")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_photo(photo=image_url, caption="Welcome! Click below to download:", reply_markup=reply_markup)

# मैसेज रिसीव और रिप्लाई करने वाला फंक्शन
async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(f"आपने कहा: {update.message.text}")

# हैंडलर्स जोड़ना
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Flask रूट सेटअप
@app.route(f"/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(), bot_app.bot)
    asyncio.run(bot_app.process_update(update))
    return "OK", 200

# बॉट स्टार्ट करने वाला मेथड
def run():
    bot_app.bot.set_webhook(url=WEBHOOK_URL)
    print(f"Webhook set at {WEBHOOK_URL}")
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    run()