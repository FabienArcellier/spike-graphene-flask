import unittest

from graphene import Schema
from graphene.test import Client

from graphene_spike.query import Query


class MainTest(unittest.TestCase):
    def setUp(self):
        self.schema = Schema(query=Query)
        self.client = client = Client(self.schema)

    def test_hello_should_work_without_argument(self):
        # Assign
        query_string = '{ hello }'

        # Acts
        executed = self.client.execute(query_string)

        # Assert
        self.assertEqual(executed['data'], {"hello": "Hello stranger, you have 18 !"})

    def test_hello_should_write_the_giving_name(self):
        # Assign
        query_string = '{ hello(name: "Fabien") }'

        # Acts
        executed = self.client.execute(query_string)

        # Assert
        self.assertEqual(executed['data'], {"hello": "Hello Fabien, you have 18 !"})
