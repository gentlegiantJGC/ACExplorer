from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TrophyMapping(SubclassBaseFile):
    ResourceType = 0x74C08007
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
