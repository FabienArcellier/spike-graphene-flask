# coding=utf-8

import unittest

from mycommand.utils import hello


class UtilsTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_hello_should_return_hello_to_the_username(self):
        # Assign
        # Acts
        hello_user = hello('fabien')
        
        # Assert
        self.assertEqual('hello fabien', hello_user)
