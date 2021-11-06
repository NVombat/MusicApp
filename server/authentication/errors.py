from core.errorfactory import AuthenticationErrors


class InvalidUserCredentialsError(AuthenticationErrors):
    ...


class InvalidVerificationError(AuthenticationErrors):
    ...


class UserDoesNotExistError(AuthenticationErrors):
    ...


class UserExistsError(AuthenticationErrors):
    ...
