# pylint: disable=invalid-name

import json

from flask import Flask, request
from graphene import Schema

from graphene_spike.query import Query

app = Flask(__name__)


@app.route('/', methods=['POST'])
def query():
    schema = Schema(query=Query)
    graphql_req = request.json
    result = schema.execute(graphql_req['query'])
    return json.dumps(result.data)

def start_flask():
    app.run()
