from pyUbiForge2.api.game import SubclassBaseFile
from .TargetTracker import TargetTracker as _TargetTracker


class MultiTargetTracker(SubclassBaseFile):
    ResourceType = 0xA102DDA7
    ParentResourceType = _TargetTracker.ResourceType
    parent: _TargetTracker

