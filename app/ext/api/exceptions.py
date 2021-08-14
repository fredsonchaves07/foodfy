class EmailAlreadyExist(Exception):
    code = 422
    message = "Email already exist."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class InvalidUser(Exception):
    code = 401
    message = "Invalid User. Consult the administrador"

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class AdminPermissionRequired(Exception):
    code = 401
    message = "Operation not allowed. Consult the administrator."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class InvalidToken(Exception):
    code = 498
    message = "Expired or invalid token."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class UserNotFound(Exception):
    code = 404
    message = "User not found."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class FileNotFound(Exception):
    code = 400
    message = "File not found"

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class ChefNotFound(Exception):
    code = 400
    message = "Chef not found"

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})
