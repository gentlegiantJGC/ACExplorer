from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AdvancedQuery(SubclassBaseFile):
    ResourceType = 0xCFF910B7
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
