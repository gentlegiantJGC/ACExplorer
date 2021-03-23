from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class MissionContext(SubclassBaseFile):
    ResourceType = 0x414FF9F7
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

