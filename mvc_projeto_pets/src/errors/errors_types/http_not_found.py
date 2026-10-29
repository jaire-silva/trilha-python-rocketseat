from .error_interface import ErrorInterface


class HttpNotFoundError(ErrorInterface):
    def __init__(self, message: str):
        super().__init__(
            message,
            name="NotFound",
            status_code=404
        )
