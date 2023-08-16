import requests


class Telegram:
    def __init__(self, bot_token: str):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    def send_message(self, chat_id, message):
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "markdown",
        }

        response = requests.post(self.base_url, json=payload)
        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print("Failed to send the message. Error:", response.text)
