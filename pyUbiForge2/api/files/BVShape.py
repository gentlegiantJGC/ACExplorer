from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class BVShape(SubclassBaseFile):
    ResourceType = 0x4EFC7705
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape
