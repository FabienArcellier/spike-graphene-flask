#!/usr/bin/python
# coding=utf-8

from __future__ import print_function

import click
from graphene import Schema
from graphene_spike.query import Query


@click.group()
def cli():
    pass


@click.command('graphene_cli')
def graphene_cli():
    schema = Schema(query=Query)

    query_string = '{ hello }'
    result = schema.execute(query_string)
    print(result.data['hello'])

    query_with_argument = '{ hello(name: "GraphQL", age: 25) }'
    result = schema.execute(query_with_argument)
    print(result.data['hello'])

    query_string = '{ goodbye }'
    result = schema.execute(query_string)
    print(result.data['goodbye'])


cli.add_command(graphene_cli)

if __name__ == '__main__':
    cli()
