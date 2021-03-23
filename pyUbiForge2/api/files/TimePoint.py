from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TimePoint(SubclassBaseFile):
    ResourceType = 0x040D27B5
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

