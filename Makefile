install:
	pip install pipenv
	pipenv install
build:
	docker build . -t hello-world:1.0
test:
	pytest hello_world
deploy:
	helm upgrade -i --namespace hello-world  hello-world ./helm

smoke-test:
	pytest smoketest
cleanup:
	kubectl delete ns hello-world
