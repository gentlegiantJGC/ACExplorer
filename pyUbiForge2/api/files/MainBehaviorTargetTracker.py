from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class MainBehaviorTargetTracker(SubclassBaseFile):
    ResourceType = 0x07894C47
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker
