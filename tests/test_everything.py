from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

# Replace 'YOUR_BOT_TOKEN' with the token provided by BotFather
TOKEN = "6599359792:AAEPZLr2zoLprDc4qZDMut5e3_fzhLSB524"


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot. Send me a message.")


def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response_message = get_response(user_message)  # Replace with your custom logic

    update.message.reply_text(response_message)


def get_response(user_input):
    # Customize this function to generate a response based on user input
    if user_input.lower() == "hello":
        return "Hi there!"
    else:
        return "I'm sorry, I don't understand that."


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register command and message handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, handle_message)
    )

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
