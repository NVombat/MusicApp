from core.errorfactory import AuthenticationErrors, ContactUsErrors


class InvalidUserCredentialsError(AuthenticationErrors):
    ...


class InvalidVerificationError(AuthenticationErrors):
    ...


class ContactUsDataInsertionError(ContactUsErrors):
    ...


class UserDoesNotExistError(AuthenticationErrors):
    ...


class TokenGenerationError(AuthenticationErrors):
    ...


class InvalidTokenError(AuthenticationErrors):
    ...


class UserExistsError(AuthenticationErrors):
    ...


class InvalidUIDError(AuthenticationErrors):
    ...
