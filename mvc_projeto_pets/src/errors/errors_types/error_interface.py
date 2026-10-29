from abc import ABC


class ErrorInterface(Exception, ABC):
    def __init__(self, message: str, name: str, status_code: int):
        super().__init__(message)
        self.message = message
        self.name = name
        self.status_code = status_code
