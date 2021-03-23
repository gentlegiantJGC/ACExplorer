from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class LocalizationPackage(SubclassBaseFile):
    ResourceType = 0x6E3C9C6F
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

