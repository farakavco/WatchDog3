import mimetypes
from watchdog3 import configuration


class URL(object):
    def __init__(self, url):
        self.url = url

    @property
    def is_relative(self):
        return not self.url.startswith('http')

    @property
    def has_primitive_slash(self):
        return self.url.startswith('/')

    @classmethod
    def is_image(cls, url):
        type_ = mimetypes.guess_type(url)[0]
        return type_ and type_.startswith('image/')

    @classmethod
    def is_video(cls, url):
        type_ = mimetypes.guess_type(url)[0]
        return type_ and type_.startswith('video/')

    def ensure_primitive_slash(self):
        if not self.has_primitive_slash:
            return '/%s' % self.url
        return self.url

    def get_full_url(self, domain, scheme='http'):
        if self.is_relative:
            return '%s://%s%s' % (scheme, domain, self.ensure_primitive_slash())
        return self.url

    @classmethod
    def is_local(cls, url):
        return '192.168.1.2' in url

    @classmethod
    def is_allowed(cls, url):
        return 'twitter' not in url and 'facebook' not in url and 'plus.google' not in url
