class DownloadCountValueError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

        self.message = "[ Error ] : type of download targets count must integer."


class DownloadCountRangeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

        self.message = "[ Error ] : download targets range to be <= 1."


class DownloadUrlValueError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

        self.message = "[ Error ] : download url is invalid."


class DownloadFilenameValueError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

        self.message = "[ Error ] : download filanem is invalid."


class DownloadFlagValueError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

        self.message = "[ Error ] : download flag must 'true' or 'false'."
