from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class WrappedShape(SubclassBaseFile):
    ResourceType = 0x6796AA1A
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape
