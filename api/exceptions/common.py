from fastapi import status
from typing import Union


class CommonException(Exception):
    def __init__(self, code: int, message: str, error: Union[Exception,None]) -> None:
        super().__init__()
        self.error = error
        self.code = code
        self.message = message


class BadRequest(CommonException):
    def __init__(self, message: str, error: Exception) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, message, error)


class NotFoundException(CommonException):
    def __init__(self, message: str) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, message, None)


class InternalServerError(CommonException):
    def __init__(self, error: Exception) -> None:
        super().__init__(
            status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal server error", error
        )


class ForbiddenException(CommonException):
    def __init__(self, message: str) -> None:
        super().__init__(status.HTTP_403_FORBIDDEN, message, None)