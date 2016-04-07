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

manual_add: http://lenz.varzesh3.com/#!/

request_timeout: 2
url_worker_threads: 128
url_queue_wait_timeout: 4


receiving_channel: '@amin'
crow_api_url: 'http://crow.farakav.com/api/message'
slack_access_token: xoxp-13319976114-20556087794-31577611078-8f47cd840d



"""

settings = None

ignore_list = None
manualy_added = None


def init():
    global settings
    global ignore_list
    global manualy_added
    settings = ConfigManager(__builtin_config)
    ignore_list = [
        'http://www.varzesh3.com/{{Url}}: 404: from http://www.varzesh3.com',
        'http://www.facebook.com/varzesh3: 404: from http://www.varzesh3.com',
        'http://taktix.varzesh3.com/: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{ VideoUrl }}: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{ SummaryUrl }}: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{{ Widget.StandingsUrl }}}: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{FilePath}}: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{Path}}: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{Thumb}}: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/resources/css/img/welcome.png: 404: from http://ads.farakav.com/clk?av=JcsN',
        'http://static2.varzesh3.com/files/insta/{{Username}}_{{MediaId}}.jpg: 404',
        'http://www.varzesh3.com/resources/css/img/hamraheman_logo.jpg: 404: from http://ads.farakav.com/clk?av=JcsN',
        'http://www.varzesh3.com/Content/assets/image/lenz-logo.png: 404: from http://lenz.varzesh3.com/#!/',
        'http://taktix.varzesh3.com/: 404: from http://www.varzesh3.com',
        'http://www.facebook.com/varzesh3: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{ VideoUrl }}: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{ SummaryUrl }}: 404: from http://www.varzesh3.com',
        'http://lenz.varzesh3.com/m/p/{{Id}}: 500: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{FilePath}}: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{Path}}: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/{{Thumb}}: 404: from http://www.varzesh3.com',
        'http://static2.varzesh3.com/files/insta/{{Username}}_{{MediaId}}.jpg: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/Static/img/logo.png: 404: from http://video.varzesh3.com/video/105403/???????????-1-2-???????-(?????-?????????)',
        'http://www.varzesh3.com/Static/img/yahoo-icon.png: 404: from http://video.varzesh3.com/video/105403/???????????-1-2-???????-(?????-?????????)',
        'http://www.varzesh3.com/{{{ Widget.StandingsUrl }}}: 404: from http://www.varzesh3.com',
        'http://www.varzesh3.com/Static/img/logo.png: 404: from http://video.varzesh3.com/video/94444/?????-?-?-????',
        'http://www.varzesh3.com/Static/img/google-icon.png: 404: from http://video.varzesh3.com/video/94444/?????-?-?-????',
        'http://www.varzesh3.com/Static/img/yahoo-icon.png: 404: from http://video.varzesh3.com/video/94444/?????-?-?-????',
        'http://www.varzesh3.com/Static/img/bottom-logo.png: 404: from http://video.varzesh3.com/video/94444/?????-?-?-????',
        'http://www.varzesh3.com/Static/img/facebook-icon.png: 404: from http://video.varzesh3.com/video/94444/?????-?-?-????',
        'http://www.varzesh3.com/loading.gif: 404: from http://charge.varzesh3.com/',
        'http://www.varzesh3.com/Content/assets/image/lenz-logo.png: 404: from http://lenz.varzesh3.com',
        'http://www.varzesh3.com/Static/img/logo.png: 404: from http://video.varzesh3.com/video/105403/???????????-1-2-???????-(?????-?????????)',
        'http://www.varzesh3.com/Static/img/google-icon.png: 404: from http://video.varzesh3.com/video/105403/???????????-1-2-???????-(?????-?????????)',
        'http://www.varzesh3.com/Static/img/facebook-icon.png: 404: from http://video.varzesh3.com/video/105403/???????????-1-2-???????-(?????-?????????)',
        'http://www.varzesh3.com/Static/img/yahoo-icon.png: 404: from http://video.varzesh3.com/video/105403/???????????-1-2-???????-(?????-?????????)'

]
    manualy_added = [
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
        'http://video.varzesh3.com/Static/img/yahoo-icon.png'
    ]
