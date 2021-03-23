from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CategoryList(SubclassBaseFile):
    ResourceType = 0x9462387E
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
