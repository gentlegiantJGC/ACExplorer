from pyUbiForge2.api.game import SubclassBaseFile
from .ValueBuffer import ValueBuffer as _ValueBuffer


class VectorBuffer(SubclassBaseFile):
    ResourceType = 0xEB870921
    ParentResourceType = _ValueBuffer.ResourceType
    parent: _ValueBuffer
