pytest:
	FLASK_ENV=test flask db migrate -m "initial configuration"
	FLASK_ENV=test flask db upgrade 
	FLASK_ENV=test pytest -v --cov=app
	rm -r app/test.db  