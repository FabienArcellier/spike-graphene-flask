## blueprint-cli-multicommands-python

[![Build Status](https://travis-ci.org/FabienArcellier/blueprint-cli-multicommands-python.svg?branch=master)](https://travis-ci.org/FabienArcellier/blueprint-cli-multicommands-python)

The goal of this spike is to implement GraphQL API based on `graphene`.

* [GraphQL in Python Made Easy](https://graphene-python.org/)
* [Build a Super Simple GraphQL Server in Flask with Graphene](https://www.youtube.com/watch?v=oQc7DC3srNM)

## Getting started

1. I check I can use graphene as local api solver from the cli

```bash
python -m graphene_spike.cli graphene_cli
```

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/blueprint-cli-multicommands-python.git
```

## Developper guideline

### Add a dependency

Write the dependency in ``setup.py``. As it's the distribution standard for pypi,
I prefer to keep ``setup.py`` as single source of truth.

I encourage avoiding using instruction as ``pipenv install requests`` to register
a new library. You would have to write your dependency in both ``setup.py`` and ``Pipfile``.

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
make install_requirements_dev
```

### Update release dependencies

Use make to instanciate a python virtual environment in ./venv and freeze
dependencies version on requirement.txt.

```bash
make update_requirements
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
make venv
source venv/bin/activate
```

### Run the linter and the unit tests

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
make lint
make tests
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
