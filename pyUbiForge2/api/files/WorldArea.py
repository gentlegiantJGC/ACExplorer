from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class WorldArea(SubclassBaseFile):
    ResourceType = 0xC76018E2
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

