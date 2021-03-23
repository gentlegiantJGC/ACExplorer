from pyUbiForge2.api.game import SubclassBaseFile
from .ValueBuffer import ValueBuffer as _ValueBuffer


class FloatBuffer(SubclassBaseFile):
    ResourceType = 0x9E29C8B1
    ParentResourceType = _ValueBuffer.ResourceType
    parent: _ValueBuffer
