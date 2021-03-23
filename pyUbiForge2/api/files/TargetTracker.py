from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TargetTracker(SubclassBaseFile):
    ResourceType = 0x209958F5
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
