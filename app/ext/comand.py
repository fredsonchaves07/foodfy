import click
from app.ext.api.services.users_services import confirm_user, create_user
from flask.cli import with_appcontext
from sqlalchemy.exc import IntegrityError


@click.command()
@with_appcontext
def user_admin():
    """Create user admin."""
    try:
        user = create_user("admin", "admin@flask-admin.com", "flask@admin", True)
        confirm_user(user.get("id"))
        click.echo("Admin user added to database")
    except IntegrityError:
        click.echo("Admin user already added to the database")


def init_app(app):
    app.cli.add_command(user_admin)
