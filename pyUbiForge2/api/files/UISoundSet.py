from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class UISoundSet(SubclassBaseFile):
    ResourceType = 0x8060D72B
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

