import requests
from watchdog3 import configuration
from watchdog3.url_ import URL
from urllib.parse import urlparse
from queue import Queue, Empty
from watchdog3.messenger import Messenger
import threading
import re
__author__ = 'amin'


class Crawler(object):
    url_patterns = [
        '<a\s+(?:[^>]*?\s+)?href="(?P<url>[^"]*)"',
        '<img\s+(?:[^>]*?\s+)?src="(?P<url>[^"]*)"'
    ]

    def __init__(self, url):
        self.url = url
        url_parts = urlparse(url)
        self.domain = url_parts.netloc
        self.scheme = url_parts.scheme
        self.urls_hash = []
        self.urls = Queue()
        self.images = Queue()
        self.messages = []
        self.image_messages = []
        self.worker_threads = {}
        self.image_worker_threads = {}

    def append_message(self, url, message):
        msg = '%s: %s' % (url, message)
        print('ERROR: %s' % msg)
        self.messages.append(msg)

    def append_image_message(self, url, message):
        msg = '%s: %s' % (url, message)
        print('ERROR: %s' % msg)
        self.image_messages.append(msg)

    def crawl(self):
        self.urls.put(self.url)
        self.url_worker()
        self.image_worker()

        for index in range(configuration.settings.img_worker_threads):
            print('Spawning image thread: %s' % index)
            new_thread = threading.Thread(target=self.image_worker, daemon=True)
            self.worker_threads[index] = new_thread
            new_thread.start()

        for index, thread_ in self.image_worker_threads.items():
            print('Waiting for thread: %s' % index)
            thread_.join()
        my_messenger = Messenger(self.image_messages)
        my_messenger.deliver_message()

        for i in range(configuration.settings.url_worker_threads):
            print('Spawning thread: %s' % i)
            new_thread = threading.Thread(target=self.url_worker, daemon=True)
            self.worker_threads[i] = new_thread
            new_thread.start()

        for i, thread in self.worker_threads.items():
            print('Waiting for thread: %s' % i)
            thread.join()
        my_messenger = Messenger(self.messages)
        my_messenger.deliver_message()

    def extract_urls(self, html_content):
        for pattern in self.url_patterns:
            for i in re.finditer(pattern, html_content, re.DOTALL):
                url = URL(i.groupdict().get('url')).get_full_url(self.domain, self.scheme)
                url_hash = hash(url)
                if url_hash not in self.urls_hash:
                    if URL.is_image(url):
                        self.urls_hash.append(url_hash)
                        self.images.put(url)
                    else:
                        self.urls_hash.append(url_hash)
                        self.urls.put(url)

    def image_worker(self):
        while True:
            try:
                url = self.images.get(timeout=configuration.settings.url_queue_wait_timeout)
            except Empty:
                break

            print('Processing %s' % url)

            try:
                response = requests.get(url, timeout=configuration.settings.request_timeout)
                if response.status_code is not 200:
                    self.append_message(url, response.status_code)
                    continue

            except Exception as ex:
                self.append_message(url, 'Following Exception Occurred: %s\n' % ex)

    def url_worker(self):
        while True:
            try:
                url = self.urls.get(timeout=configuration.settings.url_queue_wait_timeout)
            except Empty:
                break

            print('Processing %s' % url)

            try:
                if not URL.is_video(url):
                    response = requests.get(url, timeout=configuration.settings.request_timeout)
                    if response.status_code is not 200:
                        self.append_message(url, response.status_code)
                        continue

                    self.extract_urls(response.content.decode())

            except Exception as ex:
                self.append_message(url, 'Following Exception Occurred: %s\n' % ex)
