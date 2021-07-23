import pytest
from app import create_app


@pytest.fixture()
def app():
    """Inicialize app"""
    return create_app()
