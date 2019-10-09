.PHONY: docs release clean build

clean:
	rm -rf oru_env

build:
	virtualenv -p /usr/local/bin/python3 oru_env && source oru_env/bin/activate && \
		pip install -r requirements.txt

test: clean build
		source oru_env/bin/activate && \
		coverage run --source=oru setup.py test && \
		coverage html && \
		coverage report

release: test
	vim oru/__init__.py
