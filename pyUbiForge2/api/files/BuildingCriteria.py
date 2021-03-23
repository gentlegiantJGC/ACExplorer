from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class BuildingCriteria(SubclassBaseFile):
    ResourceType = 0x1BD6EEFD
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

