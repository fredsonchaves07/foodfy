from app.ext.api.exceptions import URLNotFound


def test_app_is_created(app):
    assert app.name == "app"


def test_config_is_loaded(app, config):
    assert config["DEBUG"] is False
    assert config["SEND_MAIL"] is False
    assert config["SQLALCHEMY_DATABASE_URI"] == "sqlite:///test.db"


def test_request_returns_404(client):
    response = client.get("/url_doesn't_exist!")

    assert response.status_code == URLNotFound.code
    assert response.json["message"] == URLNotFound.message
