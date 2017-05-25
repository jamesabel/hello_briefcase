#!/usr/bin/env bash
rm -r venv
~/.pyenv/versions/3.5.3/bin/python3 -m venv venv
venv/bin/pip install -U pip
venv/bin/pip install -U setuptools
venv/bin/pip install -r requirements.txt
#
