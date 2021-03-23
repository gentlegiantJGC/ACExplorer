from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ClientHandler(SubclassBaseFile):
    ResourceType = 0x43C1CB94
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

