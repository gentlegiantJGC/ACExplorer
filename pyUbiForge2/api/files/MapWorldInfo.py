from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class MapWorldInfo(SubclassBaseFile):
    ResourceType = 0x8F7EBC62
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
