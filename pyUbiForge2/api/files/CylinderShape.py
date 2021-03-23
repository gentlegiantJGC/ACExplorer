from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class CylinderShape(SubclassBaseFile):
    ResourceType = 0x445B37F9
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape
