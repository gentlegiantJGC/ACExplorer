from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class PlayerRankDetails(SubclassBaseFile):
    ResourceType = 0x5EEAF74B
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
