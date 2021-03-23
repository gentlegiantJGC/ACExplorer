from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SaveGameManager(SubclassBaseFile):
    ResourceType = 0xAF8133E7
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

