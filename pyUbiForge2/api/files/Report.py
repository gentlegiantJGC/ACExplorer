from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Report(SubclassBaseFile):
    ResourceType = 0xC38372B2
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
