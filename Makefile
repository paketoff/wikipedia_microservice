install:
	#install commands
		pip install -r requirements.txt
format: 
	#format code
	black mylib/*.py
lint:
	#flake8 or #pylint (for correct syntax)
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib test_main.py
build:
	#build container
	docker build -t deploy-fastapi .
run:
	#run docker 
	docker run -p 127.0.0.1:8080:8080 3dcf85e0852a
deploy:
	#deploy
all: install lint test deploy
