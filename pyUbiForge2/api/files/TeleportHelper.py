from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TeleportHelper(SubclassBaseFile):
    ResourceType = 0x428339E2
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
