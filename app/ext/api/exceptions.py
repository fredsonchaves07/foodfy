class BadRequestError(Exception):
    pass


class ServerError(Exception):
    code = 500
    message = "Server error."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class EmailAlreadyExist(BadRequestError):
    code = 422
    message = "Email already exist."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class InvalidUser(BadRequestError):
    code = 401
    message = "Invalid User. Consult the administrador."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class AdminPermissionRequired(BadRequestError):
    code = 401
    message = "Operation not allowed. Consult the administrator."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class InvalidToken(BadRequestError):
    code = 498
    message = "Expired or invalid token."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class UserNotFound(BadRequestError):
    code = 404
    message = "User not found."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class FileNotFound(BadRequestError):
    code = 404
    message = "File not found."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class URLNotFound(BadRequestError):
    code = 404
    message = "Api URL not found."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class MethodNotAllowed(BadRequestError):
    code = 405
    message = "Method not allowed."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})
