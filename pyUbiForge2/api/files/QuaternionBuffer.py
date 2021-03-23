from pyUbiForge2.api.game import SubclassBaseFile
from .ValueBuffer import ValueBuffer as _ValueBuffer


class QuaternionBuffer(SubclassBaseFile):
    ResourceType = 0xA8E92C14
    ParentResourceType = _ValueBuffer.ResourceType
    parent: _ValueBuffer
