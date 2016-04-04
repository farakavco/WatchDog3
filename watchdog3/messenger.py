import json
import requests


class Messenger(object):
    def __init__(self, text, receiving_channel, api_url):
        self.text = text
        self.receiving_channel = receiving_channel
        self.api_url = api_url
        self.message = {
                'text': self.text,
                'channel': self.receiving_channel
        }

    def deliver_message(self):        
        response = requests.get(self.api_url, data=self.message)

