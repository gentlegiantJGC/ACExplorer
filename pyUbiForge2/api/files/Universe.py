from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Universe(SubclassBaseFile):
    ResourceType = 0x98435A63
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
