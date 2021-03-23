from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class MeshShape(SubclassBaseFile):
    ResourceType = 0xB22B3E61
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape

