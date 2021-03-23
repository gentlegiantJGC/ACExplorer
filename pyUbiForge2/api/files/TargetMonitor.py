from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TargetMonitor(SubclassBaseFile):
    ResourceType = 0x6DEFEBDF
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
