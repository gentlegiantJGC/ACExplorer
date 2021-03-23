from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2SpawnEntityTargetTracker(SubclassBaseFile):
    ResourceType = 0x244A36A7
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker

