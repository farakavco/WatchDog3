import requests
from watchdog3 import configuration


class Messenger(object):
    def __init__(self, text_list):
        self.token = configuration.settings.slack_access_token
        self.text_list = self.normalize_text_list(text_list)
        self.receiving_channel = configuration.settings.receiving_channel

        self.message = {
                'token': self.token,
                'text': self.make_message(),
                'channel': self.receiving_channel,

        }

        self.api_url = configuration.settings.crow_api_url

    def make_message(self):
        slack_message = ''
        if self.text_list:
            for message in self.text_list:
                slack_message += '%s%s' % (message, '\n')
        else:
            slack_message += 'all links are fine'

        return self.normalize(slack_message)

    def normalize_text_list(self, text_list):
        normalized_text_list = text_list
        for text in normalized_text_list:
            if 'HTTPConnectionPool' in text or 'Read timed out' in text or 'Connection refused' in text or 'cloudfront'\
                    in text:
                normalized_text_list.remove(text)
        return normalized_text_list

    def normalize(self, message):
        normalized = message
        for ignore in configuration.ignore_list:
            if ignore in normalized:
                normalized = normalized.replace(ignore, '')

        return normalized

    def deliver_message(self):        
        response = requests.post(self.api_url, json=self.message)
        print(response.json())


if __name__ == '__main__':
    amin = Messenger('hi')
    amin.deliver_message()