from pymlconf import ConfigManager
__author__ = 'amin'


__builtin_config = """
sites:
  - http://www.varzesh3.com
mistreated_urls:
  - http://www.varzesh3.com/video
  - http://www.varzesh3.com/category
  - http://www.varzesh3.com/archive
mistreated_portal_url: http://www.varzesh3.com/PortalData/Subsystems/
request_timeout: 2
url_worker_threads: 16
url_queue_wait_timeout: 4
receiving_channel: '@moh3n'
crow_api_url: 'http://crow.farakav.com/api/message'
slack_access_token: xoxp-13319976114-20556087794-42969655874-0d1f3fc253
secret_key = KmFePUtnvQ3sXjuNq4wNVz9U2MCUtKGufsdhD324HGd
"""

settings = None

ignore_list = None
manually_added = None


def init():
    global settings
    global ignore_list
    global manually_added
    settings = ConfigManager(__builtin_config)
    ignore_list = [
        '{Url}',
        'bottom-logo.png',
        'http://ads.farakav.com',
        'http://ads.farakav.com',
        'http://ads.farakav.com',
        'http://ads.farakav.com',
        'http://ads.farakav.com',
        'http://ads.farakav.com',
        'http://ads.farakav.com',
        'http://ads.farakav.com',
        'http://www.varzesh3.com/Static/img/logo.png',
        'http://www.varzesh3.com/Content/assets/image/lenz-logo.png',
        'http://www.varzesh3.com/images/club-jiring_shixon.jpg',
        'http://www.varzesh3.com/images/007.jpg',
        'http://www.varzesh3.com/images/008.jpg',
        'http://www.varzesh3.com/images/jiring.png',
        'ConnectionPool',
        'welcome.png',
	'http://www.varzesh3.com/static2'
        'http://www.varzesh3.com/Sso/GetLoginToken',
        'hamraheman_logo',
        'twitter',
        'cloudfront.',
        'facebook',
        'loading.gif',
	'playoff',
	'playoff',
	'playoff',
        '{{ImageUrl}}',
        'http://taktix.varzesh3.com',
        '{{ VideoUrl }}',
        '{{ SummaryUrl }}',
        '{{{ Widget.StandingsUrl }}}',
        '{{FilePath}}',
        '{{Path}}',
        '{{Thumb}}',
        '{{Username}}_{{MediaId}.jpg: 404',
        '{{Id}}',
        '{{FilePath}}',
        '{{Path}}',
        '{{Thumb}}',
        '{{Username}}_{{MediaId}}',
        '{{{ Widget.StandingsUrl }}}',
        'google',
        'yahoo'
    ]
    manually_added = [
        'http://taktix.varzesh3.com/ورود'
        'http://video.varzesh3.com/Static/img/logo.png',
        'http://video.varzesh3.com/Static/img/yahoo-icon.png',
        'http://video.varzesh3.com/Static/img/logo.png',
        'http://video.varzesh3.com/Static/img/google-icon.png',
        'http://video.varzesh3.com/Static/img/yahoo-icon.png',
        'http://video.varzesh3.com/Static/img/bottom-logo.png',
        'http://video.varzesh3.com/Static/img/facebook-icon.png',
        'http://charge.varzesh3.com/loading.gif',
        'http://lenz.varzesh3.com/Content/assets/image/lenz-logo.png',
        'http://video.varzesh3.com/Static/img/logo.png',
        'http://video.varzesh3.com/Static/img/google-icon.png',
        'http://video.varzesh3.com/Static/img/facebook-icon.png',
        'http://video.varzesh3.com/Static/img/yahoo-icon.png',
        'http://lenz.varzesh3.com/Sso/GetLoginToken'


    ]
