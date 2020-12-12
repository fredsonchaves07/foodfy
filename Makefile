install:
	pip install --upgrade pip && pip install -r requirements.txt
run:
	FLASK_APP=app/app.py FLASK_ENV=development flask run