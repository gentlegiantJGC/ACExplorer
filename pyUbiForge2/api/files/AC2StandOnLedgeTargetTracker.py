from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2StandOnLedgeTargetTracker(SubclassBaseFile):
    ResourceType = 0x356AC078
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker
