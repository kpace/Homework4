class FileSystemError(Exception):
    pass


class NotEnoughSpaceError(FileSystemError):
    pass


class NodeDoesNotExistError(FileSystemError):
    pass


class DestinationNodeDoesNotExistError(NodeDoesNotExistError):
    pass


class SourceNodeDoesNotExistError(NodeDoesNotExistError):
    pass


class DestinationNodeExistError(FileSystemError):
    pass