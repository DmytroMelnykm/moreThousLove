from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from random import choice
from os import environ


DATA_SET = [
    "Ты самая лучшая",
    "Я тебя люблю больше всего",
    "Ты лучик света",
    "Ты самая самая",
    "Ты невероятная" ,
    "Такой как ты я никогда не видел",
    "Твоя улыбка самая красивая",
    "Твои глаза самые любимые",
    "Я тебя всегда найду среди толпы",
    "Ты та ради который я готов на всё",
    "Ты та которая может разтопить моё сердце",
]


def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi compliment input command /compliment")
    

def compliment(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=choice(DATA_SET))
    

def main():
    updater = Updater(environ.get("TOKEN_BOT"))

    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("compliment", compliment))

    updater.start_polling()
    updater.idle()
    

if __name__ == "__main__":
    main()