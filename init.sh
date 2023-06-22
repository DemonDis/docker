#! /bin/bash

pip install --upgrade pip

python3 -m venv .venv

. .venv/bin/activate

pip3 install -r requirements.txt