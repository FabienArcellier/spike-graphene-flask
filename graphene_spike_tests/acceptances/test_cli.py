# coding=utf-8

import unittest

import os
from click.testing import CliRunner
from mycommand.cli import cli
from mycommand_tests.acceptances.fixtures import clone_fixture


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_scenario1_contains_file_txt(self):
        with clone_fixture(fixture_name='scenario1') as wd:
            file_txt_path = os.path.join(wd, 'file.txt')
            self.assertTrue(os.path.isfile(file_txt_path))
