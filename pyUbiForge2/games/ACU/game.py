from typing import Dict, Type
import os
import json

from pyUbiForge2.api import BaseGame, BaseFile
from pyUbiForge2.api.file_object import FileDataWrapper

from .forge import ACUForge
from pyUbiForge2.api import log


FileReaders: Dict[int, Type[BaseFile]] = {}
with open(os.path.join(os.path.dirname(__file__), "resource_types.json")) as f:
    ResourceTypes = {int(_key, 16): _value for _key, _value in json.load(f).items()}


def register_file_reader(file_id: str):
    """Register a class that can read a given file id eg \"0984415E\""""
    def register_(cls):
        assert issubclass(cls, BaseFile), "The @register_file_reader can only be used with classes that subclass BaseFile"
        FileReaders[int(file_id, 16)] = cls
        return cls

    return register_


class ACUGame(BaseGame):
    ForgeClass = ACUForge
    GameIdentifier = "ACU"
    FileIDType = "Q"
    ResourceType = "I"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        super().__init__(game_directory, cache_megabytes, init)
        for file_type in FileReaders:
            if file_type not in ResourceTypes:
                log.info(f"No registered name for file type {file_type:08X}")

    def read_file(self, file: FileDataWrapper) -> BaseFile:
        file_id = file.read_file_id()
        resource_id = file.read_resource_type()
        self._call_stack.append(f"{resource_id:08X}")
        if resource_id in FileReaders:
            with file.indent:
                file_cls = FileReaders[resource_id](file_id, resource_id, file)
                self._call_stack.pop()
                return file_cls
        raise NotImplementedError(f"Not implemented {resource_id:08X}")

    @property
    def resource_types(self) -> Dict[int, str]:
        """A dictionary mapping resource type to a prettier name"""
        # implement this in subclasses
        return ResourceTypes
