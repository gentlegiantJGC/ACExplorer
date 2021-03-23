from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ObjectShape(SubclassBaseFile):
    ResourceType = 0x5A5D1303
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
