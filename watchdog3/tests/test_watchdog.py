from watchdog3 import watchdog
from watchdog3 import messenger
import unittest


class TestMessenger(object):
    def send_mail(self, mail_text):
        pass


class Test(unittest.TestCase):

    def setUpClass(cls):
        messenger.Messenger = TestMessenger

    def test_watch(self):
        urls = [
            'http://www.google.com',
            'http://www.asdsadsaddddddddddddddddddddddddddddddddddddddddddddddddd.com',
            'http://www.facebook.com'
        ]
        my_watchdog = watchdog.WatchDog(urls)
        my_watchdog.watch()


if __name__ == '__main__':
    unittest.main()