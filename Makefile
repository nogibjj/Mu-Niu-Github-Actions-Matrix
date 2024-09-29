install:
	pip install --upgrade pip && \
	pip install -r requirement.txt

format:
	black *.py

lint:
	pylint --disable=R,C main.py

test:
	python -m pytest test_main.py

all: install link test
