from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class BaseCustomActionPack(SubclassBaseFile):
    ResourceType = 0x1C2A363F
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

