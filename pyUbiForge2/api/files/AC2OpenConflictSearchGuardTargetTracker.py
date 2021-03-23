from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2OpenConflictSearchGuardTargetTracker(SubclassBaseFile):
    ResourceType = 0x6600DBA0
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker
