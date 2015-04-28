import exceptions
from directory import Directory
from file import File


class FileSystem:

    def __init__(self, size):
        self.size = size
        self.available_size = size - 1

        self.__nodes = {'/': None}

    def get_node(self, path):
        if path not in self.__nodes:
            raise exceptions.NodeDoesNotExistError

        return self.__nodes[path]

    # Не очакваме случая: directory=True и len(content) > 0
    def create(self, path, directory=False, content=''):
        if path[:path.rfind('/') + 1] not in self.__nodes:
            raise exceptions.DestinationNodeDoesNotExistError

        node_size = len(content) + 1

        if node_size > self.available_size:
            raise exceptions.NotEnoughSpaceError
        if path in self.__nodes:
            raise exceptions.DestinationNodeExistError

        if directory:
            self.__nodes[path] = Directory()
        else:
            self.__nodes[path] = File(content)

        self.available_size -= node_size


fs = File(20)
print(fs.size)