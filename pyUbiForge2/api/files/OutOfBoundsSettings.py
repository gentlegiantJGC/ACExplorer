from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class OutOfBoundsSettings(SubclassBaseFile):
    ResourceType = 0x71CD9E46
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
