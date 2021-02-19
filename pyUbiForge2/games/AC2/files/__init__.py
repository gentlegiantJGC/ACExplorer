from typing import Dict, Type
import glob
import os

from pyUbiForge2.api import BaseFile

FileReaders: Dict[int, Type[BaseFile]] = {}

_modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
__all__ = [os.path.basename(f)[:-3] for f in _modules if os.path.isfile(f) and not f.endswith('__init__.py')]


def register_file_reader(cls):
    """Register a class that can read a given file id eg \"0984415E\""""
    assert issubclass(cls, BaseFile), "The @register_file_reader can only be used with classes that subclass BaseFile"
    assert isinstance(cls.ResourceType, int), f"ResourceType is invalid for {cls}"
    assert cls.ResourceType not in FileReaders, f"Duplicate resource type {cls.ResourceType}"
    FileReaders[cls.ResourceType] = cls
    return cls

from . import *
