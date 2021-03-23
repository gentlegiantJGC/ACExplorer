from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class RegionLayout(SubclassBaseFile):
    ResourceType = 0x17FB5AA8
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
