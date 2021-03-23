from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ImpactData(SubclassBaseFile):
    ResourceType = 0x032F4C94
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

