from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FireData(SubclassBaseFile):
    ResourceType = 0xAF43CA83
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

