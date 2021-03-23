from pyUbiForge2.api.game import SubclassBaseFile
from .ObjectShape import ObjectShape as _ObjectShape


class MultiMeshShape(SubclassBaseFile):
    ResourceType = 0x9A503477
    ParentResourceType = _ObjectShape.ResourceType
    parent: _ObjectShape

