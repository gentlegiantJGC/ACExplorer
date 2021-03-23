from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class UplayMapping(SubclassBaseFile):
    ResourceType = 0x09C4884A
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
