from flask import Flask
from dynaconf import FlaskDynaconf

app = Flask(__name__)

FlaskDynaconf(app)


@app.route("/")
def index():
    return "Foodfy"


if __name__ == "__main__":
    app.run()
