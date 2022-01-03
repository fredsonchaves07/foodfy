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


class OperationNotAllowed(BadRequestError):
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


class ChefNotFound(BadRequestError):
    code = 404
    message = "Chef not found."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class MaximumImageCapacityError(BadRequestError):
    code = 400
    message = "Maximum image capacity reached. Check the required quantity."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class RecipeWithoutImage(BadRequestError):
    code = 400
    message = "At least 1 image of the recipe must be sent."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class RecipeWithoutIngredient(BadRequestError):
    code = 400
    message = "At least 1 ingredient of the recipe must be sent."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class RecipeWithoutPreparationMode(BadRequestError):
    code = 400
    message = "At least 1 preparation mode of the recipe must be sent."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class RecipeNotFound(BadRequestError):
    code = 404
    message = "Recipe not found."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class RecipeLinkedChef(BadRequestError):
    code = 401
    message = "Operation not allowed. Recipe linked to the chef."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class IncorrectLogin(BadRequestError):
    code = 401
    message = "Data access incorrect."

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})


class InvalidParameters(BadRequestError):
    code = 400
    message = "Invalid parameters in request"

    def __init__(self):
        super().__init__({"code": self.code, "message": self.message})
