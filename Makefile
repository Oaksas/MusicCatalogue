.PHONY: run-server
run-server:
	poetry run python ./musicapi/manage.py runserver

.PHONY: migrations
migrations:
	poetry run python ./musicapi/manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python ./musicapi/manage.py migrate

.PHONY: superuser
superuser:
	poetry run python ./musicapi/manage.py createsuperuser

.PHONY: update
update: install migrate;

.PHONY: install
install:
	poetry install 


