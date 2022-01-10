SHELL := /bin/bash
DIR := ${CURDIR}

test_heyu:
	source $(DIR)/env/bin/activate && python3 $(DIR)/Heyu/main.py

test_cli:
	source $(DIR)/env/bin/activate && python3 $(DIR)/Client/client.py

test_api:
	source $(DIR)/env/bin/activate && export FLASK_ENV=development && export FLASK_APP=server && cd ${DIR}/API && flask run --host=0.0.0.0 --port 6000
	
install: venv
	source $(DIR)/env/bin/activate && pip install -r requirements.txt

venv:
	python3 -m venv ./env/

