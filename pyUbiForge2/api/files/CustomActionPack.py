from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CustomActionPack(SubclassBaseFile):
    ResourceType = 0x18B9D8B1
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
