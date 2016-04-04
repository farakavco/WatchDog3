import unittest
from watchdog3 import url_
__author__ = 'amin'


class Test(unittest.TestCase):
    def test_url(self):

        has_primitive = url_.URL('/static/asds.jpg')
        non_primitive = url_.URL('static/sadsa')
        normal = url_.URL('http://varzesh3.com')
        is_image = url_.URL('http://varzesh3.com/static/asds.jpg')
        is_not_image = url_.URL('http://varzesh3.com')

        self.assertEqual(has_primitive.ensure_primitive_slash(), '/static/asds.jpg')
        self.assertEqual(non_primitive.ensure_primitive_slash(), '/static/sadsa')
        self.assertEqual(has_primitive.get_full_url('varzesh3.com'), 'http://varzesh3.com/static/asds.jpg')
        self.assertEqual(non_primitive.get_full_url('varzesh3.com'), 'http://varzesh3.com/static/sadsa')
        self.assertEqual(normal.get_full_url('varzesh3.com'), 'http://varzesh3.com')
        self.assertEqual(is_image.is_image, True)
        self.assertEqual(is_not_image.is_image, False)


if __name__ == '__main__':
    unittest.main()