class FileNotFound(Exception):
    pass


class FileParseError(Exception):
    pass


class FileParserNotFound(FileParseError):
    pass


class FileOverflowError(FileParseError):
    pass


class FileNotExhaustedError(FileParseError):
    pass
