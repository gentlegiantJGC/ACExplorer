from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class GameFixEndOfPreload(SubclassBaseFile):
    ResourceType = 0x88F73E40
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
