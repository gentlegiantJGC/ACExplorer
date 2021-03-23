from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class WorldTransitionPortal(SubclassBaseFile):
    ResourceType = 0x7C00F6AF
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
