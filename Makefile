install:
	pip install --upgrade pip && pip install -r requirements.txt
init_db:
	FLASK_APP=app/app.py FLASK_ENV=development flask db init
	FLASK_APP=app/app.py FLASK_ENV=development flask db migrate -m "initial database configuration"
	FLASK_APP=app/app.py FLASK_ENV=development flask db upgrade
run:
	FLASK_APP=app/app.py FLASK_ENV=development flask run