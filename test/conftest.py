import pytest
from app import create_app


@pytest.fixture(scope="module")
def app():
    app = create_app()
    config.init_app(app, FORCE_ENV_FOR_DYNACONF="test")
    settings.SECRET_KEY = "xd3xa6_xe94x15x8bMxe0xe8xcqFV"

    return app


@pytest.fixture(False)
def database(app):
    db.create_all()
    yield
    db.drop_all()
