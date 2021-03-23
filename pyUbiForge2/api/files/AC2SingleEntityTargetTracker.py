from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2SingleEntityTargetTracker(SubclassBaseFile):
    ResourceType = 0x945B6E13
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker

