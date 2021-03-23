from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class ReferenceListShape(SubclassBaseFile):
    ResourceType = 0x2D675BA2
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape

