from core.errorfactory import AdminErrors, AuthenticationErrors


class AdminTokenGenerationError(AuthenticationErrors):
    ...


class InvalidAdminCredentialsError(AdminErrors):
    ...


class AdminDoesNotExistError(AdminErrors):
    ...


class InvalidAdminIDError(AdminErrors):
    ...


class AdminExistsError(AdminErrors):
    ...
