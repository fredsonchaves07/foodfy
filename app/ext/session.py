from app.ext.database import db
from flask_session import Session, SqlAlchemySessionInterface

session = Session()


def init_app(app):
    session.init_app(app)
    SqlAlchemySessionInterface(app, db, "sessions", "sess_")
    return session
