from pymlconf import ConfigManager
__author__ = 'amin'


__builtin_config = """

sites:
  - http://beta.farakav.com

request_timeout: 4
url_worker_threads: 4
img_worker_threads: 16
url_queue_wait_timeout: 2


receiving_channel: '@amin'
crow_api_url: 'http://crow.farakav.com/api/message'
slack_access_token: xoxp-13319976114-20556087794-31577611078-8f47cd840d

"""

settings = None


def init():
    global settings
    settings = ConfigManager(__builtin_config)
