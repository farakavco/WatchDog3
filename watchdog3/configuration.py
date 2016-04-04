from pymlconf import ConfigManager
__author__ = 'amin'


__builtin_config = """

sites:
  - http://www.varzesh3.com
  - http://beta.farakav.com

request_timeout: 4
worker_threads: 4
url_queue_wait_timeout: 2


"""

settings = None


def init():
    global settings
    settings = ConfigManager(__builtin_config)
