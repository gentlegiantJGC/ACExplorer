from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class MissionGroup(SubclassBaseFile):
    ResourceType = 0xC0576C2D
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

