from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class ConvexVerticesShape(SubclassBaseFile):
    ResourceType = 0x53667A87
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape

