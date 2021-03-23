from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class BoxShape(SubclassBaseFile):
    ResourceType = 0x4EC68E98
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape

