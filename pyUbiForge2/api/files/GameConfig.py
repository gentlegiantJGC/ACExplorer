from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class GameConfig(SubclassBaseFile):
    ResourceType = 0x2470BC89
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

