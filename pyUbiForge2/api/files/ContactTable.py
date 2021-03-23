from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ContactTable(SubclassBaseFile):
    ResourceType = 0x5A03895E
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
