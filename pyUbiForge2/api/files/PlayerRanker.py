from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class PlayerRanker(SubclassBaseFile):
    ResourceType = 0x40573183
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

