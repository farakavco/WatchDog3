import requests
from watchdog3 import configuration
import jwt


class Messenger(object):
    def __init__(self, text_list):
        self.conf = configuration.settings
        self.receiving_channel = self.conf.receiving_channel
        self.ignore_list = self.conf.ignore_list
        self.slack_message = ''
        self.text_list = self.normalize(text_list)
        self.make_message()
        self.message = {
                'text': self.slack_message,
                'channel': self.receiving_channel,
        }
        self.api_url = self.conf.crow_api_url

    def normalize(self, message):
        return [item for item in message if not [ignore for ignore in self.ignore_list if ignore in item]]

    def authenticate(self):
        return jwt.encode({'token': self.conf.slack_access_token}, self.conf.secret_key)

    def make_headers(self):
        return {'X-JWT-Token': self.authenticate()}

    def make_message(self):
        if self.text_list:
            for message in self.text_list:
                self.slack_message += '%s%s' % (message, '\n')
        else:
            self.slack_message = 'all fine'

    def deliver_message(self):
        print(requests.post(self.api_url, json=self.message, headers=self.make_headers()).text)
