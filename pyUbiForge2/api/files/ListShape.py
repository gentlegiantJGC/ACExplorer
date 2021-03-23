from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class ListShape(SubclassBaseFile):
    ResourceType = 0x86EBFD8D
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape

