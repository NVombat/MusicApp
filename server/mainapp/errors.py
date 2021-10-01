from core.errorfactory import MusicDataErrors


class FileAlreadyExistsForCurrentUserError(MusicDataErrors):
    ...


class FileDoesNotExistForCurrentUserError(MusicDataErrors):
    ...
