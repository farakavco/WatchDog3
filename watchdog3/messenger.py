import requests
from watchdog3 import configuration


class Messenger(object):
    def __init__(self, text_list):
        self.token = configuration.settings.slack_access_token
        self.text_list = self.normalize(text_list)
        self.receiving_channel = configuration.settings.receiving_channel

        self.message = {
                'token': self.token,
                'text': self.make_message(),
                'channel': self.receiving_channel,
        }

        self.api_url = configuration.settings.crow_api_url

    def normalize(self, message):
        normalized = message
        for ignore in configuration.ignore_list:
            for item in normalized:
                if ignore in item:
                    normalized.remove(item)
                # continue
        return normalized

    def make_message(self):
        slack_message = ''
        if self.text_list:
            slack_message = '%s%s' % ('Result of WatchDog Scouting Varzesh3 Links: These Links Appear to Have Problem',
                                      '\n')
            for message in self.text_list:
                slack_message += '%s%s' % (message, '\n')
        else:
            slack_message += 'all links are fine'
        print(slack_message)
        return slack_message

    def deliver_message(self):
        print('this is slack message %s' % self.message['text'])
        response = requests.post(self.api_url, json=self.message)
        print(response.json())


if __name__ == '__main__':
    amin = Messenger('hi')
    amin.deliver_message()