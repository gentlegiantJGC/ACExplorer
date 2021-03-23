from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class MultiTargetTracker2(SubclassBaseFile):
    ResourceType = 0x52C68A9B
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker

