from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# अपना BotFather से मिला टोकन यहां डालें
TOKEN = "8007060492:AAFNr28xUM6QnX4w6AIRrj2Um43ZpEa_5ZU"

# /start कमांड का फंक्शन
async def start(update: Update, context: CallbackContext):
    # इमेज URL
    image_url = "https://envs.sh/Q0_.jpg"

    # इनलाइन बटन बनाना
    keyboard = [
        [InlineKeyboardButton("🔽 Download 1", url="https://example.com/download1"),
         InlineKeyboardButton("🔽 Download 2", url="https://example.com/download2")],
        [InlineKeyboardButton("🔽 Download 3", url="https://example.com/download3")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # इमेज और बटन भेजना
    await update.message.reply_photo(photo=image_url, caption="Welcome! Click below to download:", reply_markup=reply_markup)

# मैसेज रिसीव और रिप्लाई करने वाला फंक्शन
async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(f"आपने कहा: {update.message.text}")

# बॉट को स्टार्ट करने वाला मेथड
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()