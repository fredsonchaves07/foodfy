import sys
import traceback

from app.ext.api.exceptions import MethodNotAllowed, URLNotFound
from flask import current_app, request


def response_error(error):
    return {"code: ": error.code, "message": error.message}, error.code


def url_not_found(error):
    return {
        "code: ": URLNotFound.code,
        "message": URLNotFound.message,
    }, URLNotFound.code


def method_not_allowed(error):
    return {
        "code: ": MethodNotAllowed.code,
        "message": MethodNotAllowed.message,
    }, MethodNotAllowed.code


def server_error(error):
    exc_type, exc_value, exc_traceback = sys.exc_info()

    file_path = traceback.extract_tb(exc_traceback)[-1].filename
    detail_line = traceback.extract_tb(exc_traceback)[-1].line
    line_number = traceback.extract_tb(exc_traceback)[-1].lineno

    current_app.logger.error(
        {
            "error: ": error,
            "route": request.url,
            "file_path": file_path,
            "line_number": line_number,
            "detail_line: ": detail_line,
        }
    )

    return {"code: ": 500, "message": "Server error"}, 500
