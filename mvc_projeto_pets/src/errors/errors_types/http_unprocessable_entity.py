from .error_interface import ErrorInterface


class HttpUnprocessableEntityError(ErrorInterface):
    def __init__(self, message: str):
        super().__init__(
            message,
            name="UnprocessableEntity",
            status_code=422
        )
