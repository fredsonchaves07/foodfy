class EmailAlreadyExist(Exception):
    code = 422
    message = "Email already exist."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class AdminPermissionRequired(Exception):
    code = 401
    message = "Operation not allowed. Consult the administrator"

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})
