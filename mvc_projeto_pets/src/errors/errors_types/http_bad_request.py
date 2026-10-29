from .error_interface import ErrorInterface


class HttpBadRequestError(ErrorInterface):
    def __init__(self, message: str):
        super().__init__(
            message,
            name="BadRequest",
            status_code=400
        )
