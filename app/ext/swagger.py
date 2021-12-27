from flasgger import Swagger

swagger_config = {
    "info": {
        "title": "A Foodfy API",
        "description": "Foodfy Document API",
        "contact": {"email": "fredsonchaves07@gmail.com"},
        "license": {
            "name": "MIT",
            "url": "https://github.com/fredsonchaves07/foodfy/blob/main/LICENSE",
        },
    },
    "headers": [
        ("Access-Control-Allow-Origin", "*"),
        ("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"),
        ("Access-Control-Allow-Credentials", "true"),
    ],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/",
}
swagger = Swagger(config=swagger_config)


def init_app(app):
    swagger.init_app(app)
