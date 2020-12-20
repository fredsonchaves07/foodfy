install:
	pip install --upgrade pip && pip install -r requirements.txt
dev:
	export FLASK_APP=app/app.py && export FLASK_ENV=development
init_db:
	flask db init
	flask db migrate -m "initial database configuration"
	flask db upgrade
run:
	flask run