import unittest
from watchdog3 import link_extractor, url_


class Test(unittest.TestCase):
    def test_link_extractor(self):
        test_snippet = """
 <div id="social">
                <a target="_blank"
                href="http://www.facebook.com/varzesh3"><img width="23"
                height="23" class="img" src="/static/img/facebook.png" alt="Facebook" /></a>
                <a target="_blank" href="http://instagram.com/varzesh3"><img width="23" height="23" class="img" src="/static/img/instagram.png" alt="Instagram" /></a>
                <a target="_blank" href="https://twitter.com/varzesh3"><img width="23" height="23" class="img" src="/static/img/twitter24.png" alt="Twitter" /></a>
                <a href="http://www.varzesh3.com/rss/index" target="_blank"><img alt="RSS" width="23" height="23" src="/static/img/RSS.png"></a>
            </div>

"""
        extractor = link_extractor.LinkExtractor(test_snippet)
        links = [i.get_full_url('varzesh3.com') for i in extractor.extract()]
        print(list(links))
        self.assertEqual(sorted(links), sorted([
            'http://www.facebook.com/varzesh3',
            'http://varzesh3.com/static/img/facebook.png',
            'http://instagram.com/varzesh3',
            'http://varzesh3.com/static/img/instagram.png',
            'https://twitter.com/varzesh3',
            'http://varzesh3.com/static/img/twitter24.png',
            'http://www.varzesh3.com/rss/index',
            'http://varzesh3.com/static/img/RSS.png',
        ]))
        # expected = "http://varzesh3.com/users/2174408/ahmad"
        # result = url_.URL(link).get_full_url('varzesh3.com')
        # self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


