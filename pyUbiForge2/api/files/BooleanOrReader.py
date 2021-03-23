from pyUbiForge2.api.game import SubclassBaseFile
from .BooleanOperationInputReader import (
    BooleanOperationInputReader as _BooleanOperationInputReader,
)


class BooleanOrReader(SubclassBaseFile):
    ResourceType = 0x1120EFDE
    ParentResourceType = _BooleanOperationInputReader.ResourceType
    parent: _BooleanOperationInputReader
