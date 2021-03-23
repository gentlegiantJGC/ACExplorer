from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class TransformShape(SubclassBaseFile):
    ResourceType = 0xAA63E732
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape
