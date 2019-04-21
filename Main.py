import TelegramNotifier


def main():

    token = "TOKEN_HERE"
    chat_id = "INTEGER CHAT ID HERE"

    # token = os.environ['TG_BOT_TOKEN']
    # chat_id = os.environ['TG_CHAT_ID']

    tn = TelegramNotifier(token=token, chat_id=chat_id)

    notifier_text = {"Stage": "Client-ETL",
                     "Client": "123",
                     "Campaign": "456",
                     "ERROR": "An Error has occurred"}

    message = tn.format_message(notifier_text)

    tn.send_message(message, parse_mode="html")


if __name__ == "__main__":
    main()
