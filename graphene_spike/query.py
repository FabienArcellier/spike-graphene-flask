# pylint: disable=unused-argument

from graphene import ObjectType, String, Int


class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"), age=Int(default_value=18))
    goodbye = String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(self, info, name, age):
        return f'Hello {name}, you have {age} !'

    def resolve_goodbye(self, info):
        return 'See ya!'
