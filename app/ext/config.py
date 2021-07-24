from dynaconf import FlaskDynaconf


def init_app(app, **kwargs):
    FlaskDynaconf(app, **kwargs)
    app.config.load_extensions("EXTENSIONS")
