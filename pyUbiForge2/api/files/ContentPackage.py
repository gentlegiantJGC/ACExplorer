from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ContentPackage(SubclassBaseFile):
    ResourceType = 0x4DB4B1FE
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
