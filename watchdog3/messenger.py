import requests
from watchdog3 import configuration
import jwt


class Messenger(object):
    def __init__(self, text_list):
        self.text_list = self.normalize(text_list)
        self.receiving_channel = configuration.settings.receiving_channel

        self.message = {
                'text': self.make_message(),
                'channel': self.receiving_channel,
        }

        self.api_url = configuration.settings.crow_api_url

    def normalize(self, message):
        normalized = []
        ignore_list = configuration.ignore_list
        for ignore in ignore_list:
            for item in message:
                if ignore not in item:
                    normalized.append(item)
        return normalized

    def make_message(self):
        slack_message = ''
        if self.text_list:
            slack_message = '%s%s' % (configuration.settings.report_message,
                                      '\n')
            for message in self.text_list:
                slack_message += '`%s%s' % (message, '`\n')
        else:
            slack_message += 'all links are fine'
        print(slack_message)
        return slack_message

    def authenticate(self):
        authentication = {
            'token': configuration.settings.slack_access_token
        }
        return jwt.encode(authentication, configuration.settings.secret_key)

    def make_headers(self):
        return {
            'X-JWT-Token': self.authenticate()
        }

    def deliver_message(self):
        print('this is slack message %s' % self.message['text'])

        response = requests.post(self.api_url, json=self.message, headers=self.make_headers())
        print(response.text)


if __name__ == '__main__':
    amin = Messenger('hi')
    amin.deliver_message()
