from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class CapsuleShape(SubclassBaseFile):
    ResourceType = 0xB8599052
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape

