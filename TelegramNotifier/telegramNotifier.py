"""
The telegramNotifier is responsible for sending notification messages to a given channel via a specific bot.
"""

__author__ = ["Aashima Yuthika", "Darshil Chanpura"]
__credits__ = ["Aashima Yuthika", "Darshil Chanpura", "Bhavik Patel"]
__version__ = "1.0"
__status__ = "Development"

import requests


class TelegramNotifier(object):

    def __init__(self, token, chat_id):
        self.token = token
        self.url = "https://api.telegram.org/bot{}/".format(token)
        self.chat_id = chat_id

    @staticmethod
    def post_url(url, params):
        """
        This function sends the post request to the given URL with the specified parameters

        :param url: The URL to which the request is to be sent
        :param params: The parameters for the request

        :return: Returns the response of the post request
        """
        response = requests.post(url, json=params)
        content = response.content.decode("utf8")
        return content

    @staticmethod
    def format_message(formatter_text):
        """
        This function is responsible for formatting the message that is to be sent to the notifier.

        :param formatter_text: Dictionary containing the key-value pair containing
        all the information that needs to be displayed

        :return: Returns the formatted message (in html format) to be send to the notifications channel
        """
        formatter_keys = formatter_text.keys()

        formatted_message = ""

        for k in formatter_keys:
            formatted_message = formatted_message + "<b>{key}</b> : <em>{text}</em>\n".format(key=k, text=str(formatter_text[k]))
        return formatted_message

    def send_message(self, text, **params):
        """
        This function is responsible for sending the notification to the specified notifications channel.

        :param text: The notification message that is to be sent
        :param params: Any other parameters that are required for sending the message

        :return: Returns nothing
        """
        message_url = self.url + "sendMessage"
        params["text"] = text
        params["chat_id"] = self.chat_id
        self.post_url(message_url, params)
