from core.telegram.telegram import Telegram
from configs.config import chat_id, bot_token


def main():
    telegram = Telegram(bot_token)
    message = "Hello world"
    telegram.send_message(chat_id, message)


if __name__ == "__main__":
    main()
