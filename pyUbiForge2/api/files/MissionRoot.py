from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class MissionRoot(SubclassBaseFile):
    ResourceType = 0xE6545731
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

