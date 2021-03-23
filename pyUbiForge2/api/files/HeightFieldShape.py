from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class HeightFieldShape(SubclassBaseFile):
    ResourceType = 0x0F0EECBB
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape
