# pylint: disable=invalid-name

import json

from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema

from graphene_spike.query import Query

app = Flask(__name__)


app.add_url_rule('/', view_func=GraphQLView.as_view('query', schema=Schema(query=Query), graphiql=True))


def start_flask():
    app.run()
