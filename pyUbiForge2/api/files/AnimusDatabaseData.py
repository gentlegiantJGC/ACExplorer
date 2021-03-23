from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AnimusDatabaseData(SubclassBaseFile):
    ResourceType = 0x6A964E76
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
