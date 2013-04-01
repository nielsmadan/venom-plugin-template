import unittest
from nose.tools import eq_

import vim_stub
import venom_stub

import helloworld

class TestGreeting(unittest.TestCase):
    def test_get_greeting(self):
        result = helloworld.greetings._get_greeting()

        eq_(result, "Hello World")
