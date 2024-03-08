run-server:
	poetry run python ./musicapi/manage.py runserver

migrations:
	poetry run python ./musicapi/manage.py makemigrations

migrate:
	poetry run python ./musicapi/manage.py migrate

superuser:
	poetry run python ./musicapi/manage.py createsuperuser

update: install migrate;

install:
	poetry install 
