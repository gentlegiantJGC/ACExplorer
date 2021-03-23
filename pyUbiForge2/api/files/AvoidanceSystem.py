from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AvoidanceSystem(SubclassBaseFile):
    ResourceType = 0x9846A3B5
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
