from core.errorfactory import MusicDataErrors


class FileDoesNotExistForCurrentUserError(MusicDataErrors):
    ...


class ProfileDataUnavailableError(MusicDataErrors):
    ...
