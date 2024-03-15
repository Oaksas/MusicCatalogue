.PHONY: run-server
run-server:
	poetry run python3 ./musicapi/manage.py runserver

.PHONY: migrations
migrations:
	poetry run python3 ./musicapi/manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python3 ./musicapi/manage.py migrate

.PHONY: superuser
superuser:
	poetry run python3 ./musicapi/manage.py createsuperuser

.PHONY: update
update: install migrate;

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit  install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files
