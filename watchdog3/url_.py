import mimetypes


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
    def normalize(cls, url):
        if url.startswith('http://www.varzesh3.com/video') or url.startswith('http://www.varzesh3.com/category') or\
                url.startswith('http://www.varzesh3.com/archive'):
            normalized = url.replace('http://www.', 'http://video.')
            return normalized

        return url

