from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class MissionHistory(SubclassBaseFile):
    ResourceType = 0x84A80CC2
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
