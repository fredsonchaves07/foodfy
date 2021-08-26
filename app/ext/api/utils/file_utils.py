import os
from datetime import datetime

from dynaconf import settings


def upload(file):
    filename = f"{datetime.now()}-{file.filename}"

    dir_path = os.path.dirname(os.path.realpath(__name__))
    path = os.path.join(settings.get("UPLOAD_FOLDER"), filename)

    file.save(dir_path + path)

    return {"filename": filename, "path": path}


def remove(file):
    dir_path = os.path.dirname(os.path.realpath(__name__))

    os.remove(dir_path + file.path)
