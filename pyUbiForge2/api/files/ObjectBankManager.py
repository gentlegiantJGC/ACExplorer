from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ObjectBankManager(SubclassBaseFile):
    ResourceType = 0x54243032
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
