from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# अपना BotFather से मिला टोकन यहां डालें
TOKEN = "8007060492:AAFNr28xUM6QnX4w6AIRrj2Um43ZpEa_5ZU"

# स्टार्ट कमांड का फंक्शन
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("नमस्ते! मैं आपका टेलीग्राम बॉट हूँ।")

# मैसेज रिसीव और रिप्लाई करने वाला फंक्शन
async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(f"आपने कहा: {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
