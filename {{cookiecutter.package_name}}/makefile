all: install

install: 
	pip install -r requirements.txt
	pip install .

dev: 
	pip install -r requirements-dev.txt
	pip install -e .

freeze: 
	pip freeze | sort | grep -v '{{ cookiecutter.package_name }}'
test: 
	cd tests && ( pytest -rXxs -vv --cov-report html --cov-report term-missing --cov {{ cookiecutter.package_name }} )

doc: 
	cd docs && make html

