from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Graph(SubclassBaseFile):
    ResourceType = 0xC8842AD8
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
