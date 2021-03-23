from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2GroupTargetTracker(SubclassBaseFile):
    ResourceType = 0x5DC5AACF
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker

