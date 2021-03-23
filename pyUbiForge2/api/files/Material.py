from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Material(SubclassBaseFile):
    ResourceType = 0x85C817C3
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

