import pytest
from app import create_app
from app.ext.database import db


@pytest.fixture()
def app():
    """Inicialize app"""
    return create_app()


@pytest.fixture(False)
def database(app):
    db.create_all()
    yield
    db.drop_all()
