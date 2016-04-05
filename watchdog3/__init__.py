from watchdog3 import configuration
from watchdog3.crawler import Crawler
import sys
__author__ = 'amin'
__version__ = '0.2.0a'


def main():
    configuration.init()
    for site in configuration.settings.sites:
        Crawler(site).crawl()
    sys.exit(0)
