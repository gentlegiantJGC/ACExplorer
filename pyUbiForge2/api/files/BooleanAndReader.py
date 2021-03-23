from pyUbiForge2.api.game import SubclassBaseFile
from .BooleanOperationInputReader import (
    BooleanOperationInputReader as _BooleanOperationInputReader,
)


class BooleanAndReader(SubclassBaseFile):
    ResourceType = 0xFA76C079
    ParentResourceType = _BooleanOperationInputReader.ResourceType
    parent: _BooleanOperationInputReader
