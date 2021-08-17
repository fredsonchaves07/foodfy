import os
from datetime import datetime

from app.ext.api.exceptions import FileNotFound
from dynaconf import settings


def upload(file):
    if not file:
        raise FileNotFound

    filename = f"{datetime.now()}-{file.filename}"
    path = os.path.join(settings.get("UPLOAD_FOLDER"), filename)

    file.save(path)

    return {"filename": filename, "path": path}


def remove(file):
    if not file:
        raise FileNotFound

    os.remove(file.path)
