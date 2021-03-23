from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AODataPackage(SubclassBaseFile):
    ResourceType = 0x489B9085
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
