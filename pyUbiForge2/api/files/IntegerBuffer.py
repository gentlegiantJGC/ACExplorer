from pyUbiForge2.api.game import SubclassBaseFile
from .ValueBuffer import ValueBuffer as _ValueBuffer


class IntegerBuffer(SubclassBaseFile):
    ResourceType = 0xD1F05B45
    ParentResourceType = _ValueBuffer.ResourceType
    parent: _ValueBuffer
