pytest:
	FLASK_ENV=test poetry run pytest -v --cov=app
	rm -r tmp/*test*