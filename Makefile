build:
	docker build . -t hello-world:1.0
test:
	docker-compose build
	docker-compose run test
deploy:
	helm upgrade -i hello-world ./helm
smoke-test:
	pytest smoketest