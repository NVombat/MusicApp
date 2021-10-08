from core.errorfactory import AWSErrors, MusicDataErrors


class FileAlreadyExistsForCurrentUserError(MusicDataErrors):
    ...


class FileDoesNotExistForCurrentUserError(MusicDataErrors):
    ...


class DataFetchingError(MusicDataErrors):
    ...


class AWSUploadError(AWSErrors):
    ...
