PYTHON_INTERPRETER = python3

build: clean deps_pkg
	mkdir ./dist
	cp ./src/main/main.py ./dist/
	zip -r ./dist/jobs.zip src
	cd ./libs && zip -r ../dist/libs.zip .

zip_jobs:
	mkdir -p ./dist
	cp ./src/main/main.py ./dist/
	zip -r ./dist/jobs.zip src

clean: .clean-build .clean-pyc .clean-test

.clean-build:
	rm -fr dist/

.clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +



.clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/


deps_dev:
	$(PYTHON_INTERPRETER) -m pip install -U -r requirements.txt

deps_pkg:
	$(PYTHON_INTERPRETER) -m pip install --upgrade --force-reinstall -r requirements_pkg.txt -t ./libs

local_submit: zip_jobs
	gluesparksubmit --master local  --py-files ./dist/jobs.zip ./dist/main.py "--JOB_NAME=twitter_job"
