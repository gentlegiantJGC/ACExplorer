from pyUbiForge2.api.game import SubclassBaseFile
from .BooleanButtonReader import BooleanButtonReader as _BooleanButtonReader


class PadBooleanButtonReader(SubclassBaseFile):
    ResourceType = 0x682B1FDA
    ParentResourceType = _BooleanButtonReader.ResourceType
    parent: _BooleanButtonReader

