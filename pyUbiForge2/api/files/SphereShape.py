from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class SphereShape(SubclassBaseFile):
    ResourceType = 0xFA3F7A18
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape
