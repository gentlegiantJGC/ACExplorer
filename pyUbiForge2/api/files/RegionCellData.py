from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class RegionCellData(SubclassBaseFile):
    ResourceType = 0xB6F1472B
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

