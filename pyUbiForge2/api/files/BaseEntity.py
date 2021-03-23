from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class BaseEntity(SubclassBaseFile):
    ResourceType = 0x71CA3FC0
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

