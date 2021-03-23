from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CollisionMaterial(SubclassBaseFile):
    ResourceType = 0x74F7311D
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

