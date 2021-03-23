from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Skeleton(SubclassBaseFile):
    ResourceType = 0x24AECB7C
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

