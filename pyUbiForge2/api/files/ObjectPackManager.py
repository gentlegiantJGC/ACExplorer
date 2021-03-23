from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ObjectPackManager(SubclassBaseFile):
    ResourceType = 0x53F1AA6F
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

