from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class GameBootstrap(SubclassBaseFile):
    ResourceType = 0xE5A83560
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
