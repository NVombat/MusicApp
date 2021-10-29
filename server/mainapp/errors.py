from core.errorfactory import AWSErrors, MusicDataErrors


class FileAlreadyExistsForCurrentUserError(MusicDataErrors):
    ...


class FileDoesNotExistForCurrentUserError(MusicDataErrors):
    ...


class ProfileDataUnavailableError(MusicDataErrors):
    ...


class DataFetchingError(MusicDataErrors):
    ...


class AWSDownloadError(AWSErrors):
    ...


class AWSUploadError(AWSErrors):
    ...
