from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
BOT_TOKEN = 7316950091:AAH5zH6XIPL18bRaUhm-e0EMB-kcZWOtWiM
# Replace 'YOUR_CHAT_ID' with the chat ID of the organization
CHAT_ID = 7316950091

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Send your message, and it will be forwarded anonymously.')

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    context.bot.send_message(chat_id=CHAT_ID, text=f"Anonymous message: {user_message}")

def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
