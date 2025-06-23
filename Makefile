build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

lint:
	uv run flake8 task_manager

install:
	uv sync

start:
	python manage.py runserver

collectstatic:
	python manage.py collectstatic --noinput

migrate:
	python manage.py migrate