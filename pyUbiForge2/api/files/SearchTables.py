from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SearchTables(SubclassBaseFile):
    ResourceType = 0x25D7F39A
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

