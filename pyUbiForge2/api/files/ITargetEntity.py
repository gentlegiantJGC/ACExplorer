from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ITargetEntity(SubclassBaseFile):
    ResourceType = 0x699FF698
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
