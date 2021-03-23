from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AnimusDatabaseCodex(SubclassBaseFile):
    ResourceType = 0x1F659993
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

