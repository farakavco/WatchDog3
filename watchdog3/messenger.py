import requests
from watchdog3 import configuration
import jwt


class Messenger(object):
    def __init__(self, text_list):
        self.messages = text_list

    def deliver_message(self):
        with open('log', 'w', encoding='utf-8') as log:
            for message in self.messages:
                log.write('%s\n' % message)

