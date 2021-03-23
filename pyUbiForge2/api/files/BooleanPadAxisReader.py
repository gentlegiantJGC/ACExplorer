from pyUbiForge2.api.game import SubclassBaseFile
from .PadAxisReader import PadAxisReader as _PadAxisReader


class BooleanPadAxisReader(SubclassBaseFile):
    ResourceType = 0xD824A5C1
    ParentResourceType = _PadAxisReader.ResourceType
    parent: _PadAxisReader

