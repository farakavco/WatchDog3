import requests
from watchdog3 import configuration


class Messenger(object):
    def __init__(self, text):
        self.token = configuration.settings.slack_access_token
        self.text = text
        self.slack_message = ''
        self.receiving_channel = configuration.settings.receiving_channel
        self.fine_status_message = {
                'token': self.token,
                'text': 'EveryThing is fine',
                'channel': self.receiving_channel,
        }
        self.message = {
                'token': self.token,
                'text': 'sd',
                'channel': self.receiving_channel,

        }

        self.make_message()

        self.api_url = configuration.settings.crow_api_url

    def make_message(self):
        if self.text:
            for message in self.text:
                self.slack_message += '%s%s' % (message, '\n')
        else:
            self.slack_message += '%s' % self.fine_status_message

    def deliver_message(self):        
        response = requests.post(self.api_url, json=self.message)
        print(response)


if __name__ == '__main__':
    amin = Messenger('hi')
    amin.deliver_message()