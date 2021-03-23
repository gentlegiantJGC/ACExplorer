from pyUbiForge2.api.game import SubclassBaseFile
from .BooleanReader import BooleanReader as _BooleanReader


class BooleanButtonReader(SubclassBaseFile):
    ResourceType = 0xE4A9FE20
    ParentResourceType = _BooleanReader.ResourceType
    parent: _BooleanReader
