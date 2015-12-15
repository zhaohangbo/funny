from unittest import TestCase

import pyfun

class TestJoke(TestCase):
    def test_is_string(self):
        s = pyfun.joke()
        self.assertTrue(isinstance(s, basestring))
