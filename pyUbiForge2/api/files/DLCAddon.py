from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class DLCAddon(SubclassBaseFile):
    ResourceType = 0x14F43DD7
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
