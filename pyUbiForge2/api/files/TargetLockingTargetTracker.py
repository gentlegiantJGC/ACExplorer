from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class TargetLockingTargetTracker(SubclassBaseFile):
    ResourceType = 0xF1AD71A5
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker

