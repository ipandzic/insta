delete-migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

migrate:
	python manage.py makemigrations
	python manage.py migrate