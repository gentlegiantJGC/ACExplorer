from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FXInstance(SubclassBaseFile):
    ResourceType = 0x67C0F01E
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

