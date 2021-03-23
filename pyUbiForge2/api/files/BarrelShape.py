from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class BarrelShape(SubclassBaseFile):
    ResourceType = 0x97CD8890
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape

