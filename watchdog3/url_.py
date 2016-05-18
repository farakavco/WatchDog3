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
    def is_ad(cls, url):
        return 'ads.farakav' in url

    @classmethod
    def is_image(cls, url):
        type_ = mimetypes.guess_type(url)[0]
        return type_ and type_.startswith('image/')

    @classmethod
    def is_video(cls, url):
        type_ = mimetypes.guess_type(url)[0]
        return type_ and type_.startswith('video/')

    @classmethod
    def is_lenz(cls, url):
        return url.startswith('lenz.')

    def ensure_primitive_slash(self):
        if not self.has_primitive_slash:
            return '/%s' % self.url
        return self.url

    def get_full_url(self, domain, scheme='http'):
        if self.is_relative:
            return '%s://%s%s' % (scheme, domain, self.ensure_primitive_slash())
        return self.url

    @classmethod
    def normalize(cls, url):
        for mistreated_url in configuration.settings.mistreated_urls:
            if url.startswith(mistreated_url):
                normalized = url.replace('http://www.', 'http://video.')
                return normalized

        if url.startswith(configuration.settings.mistreated_portal_url):
            normalized = url.replace('http://www.', 'http://sms.')
            return normalized

        return url

    @classmethod
    def is_allowed(cls, url, level):
        return (not URL.is_ad(url) and not URL.is_video(url) and
                ((level is 0 or level is 1) or (level is 2 and (URL.is_image(url)))))

