from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SaveGame(SubclassBaseFile):
    ResourceType = 0xBDBE3B52
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

