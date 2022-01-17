run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

teste:
	python manage.py test

check:
	python manage.py check