from urllib.parse import urlparse
from queue import Queue, Empty
import threading
import re
import requests
from watchdog3 import configuration
from watchdog3.url_ import URL
from watchdog3.messenger import Messenger

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
        self.messages = []
        self.worker_threads = {}
        self.image_worker_threads = {}

    def append_message(self, url, message, parent_url):
        msg = '%s: %s: from %s' % (url, message, parent_url)
        print('ERROR: %s' % msg)
        self.messages.append(msg)

    def crawl(self):
        # Adding urls from config
        self.urls.put((0, '', self.url))

        for i in range(configuration.settings.url_worker_threads):
            new_thread = threading.Thread(target=self.url_worker, daemon=True)
            self.worker_threads[i] = new_thread
            new_thread.start()

        for i, thread in self.worker_threads.items():
            thread.join()
        my_messenger = Messenger(self.messages)
        my_messenger.deliver_message()

    def extract_urls(self, html_content, level, parent_url):
        for pattern in self.url_patterns:
            for i in re.finditer(pattern, html_content, re.DOTALL):
                url = URL(i.groupdict().get('url')).get_full_url(self.domain, self.scheme)
                url_hash = hash(url)
                if url_hash not in self.urls_hash:
                        self.urls_hash.append(url_hash)
                        self.urls.put((level, parent_url, url))

    def url_worker(self):
        while True:
            try:
                level, parent_url, url = self.urls.get(timeout=configuration.settings.url_queue_wait_timeout)
            except Empty:
                break
            try:
                print('Processing %s' % url)
                if URL.is_local(url) and URL.is_allowed(url):
                    response = requests.get(url, timeout=4)
                    if response.status_code is not 200:
                        self.append_message(url, response.status_code, parent_url)
                        continue
                    if not URL.is_image(url) and not URL.is_video(url):
                        self.extract_urls(response.content.decode(), level+1, url)

            except Exception as ex:
                self.append_message(url, 'Following Exception Occurred: %s\n' % ex, parent_url)
