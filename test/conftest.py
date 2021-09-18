import pytest
from app import create_app
from app.ext.api.models.user import User
from app.ext.api.services import token_services
from app.ext.database import db
from dynaconf import settings


@pytest.fixture()
def app():
    app = create_app()

    return app


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="test")


@pytest.fixture()
def database(app):
    db.create_all()
    yield
    db.drop_all()


@pytest.fixture()
def admin_user(database):
    user = User()

    user.name = "admin user"
    user.email = "admin@email.com"
    user.password = "admin"
    user.is_admin = True
    user.confirmed = True

    db.session.add(user)
    db.session.commit()

    token = token_services.generate_token(user.id, user.email)

    admin = {"id": user.id, "email": user.email, "token": token}

    return admin
