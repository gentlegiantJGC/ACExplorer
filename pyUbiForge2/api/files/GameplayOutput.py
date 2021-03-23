from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class GameplayOutput(SubclassBaseFile):
    ResourceType = 0xE2CB024F
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
