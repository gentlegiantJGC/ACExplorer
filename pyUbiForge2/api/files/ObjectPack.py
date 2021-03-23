from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ObjectPack(SubclassBaseFile):
    ResourceType = 0xF29157B2
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

