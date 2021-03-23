from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FastTravelEntry(SubclassBaseFile):
    ResourceType = 0x9FF4770F
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
