from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2GroupManipulationTargetTargetTracker(SubclassBaseFile):
    ResourceType = 0xAB43791F
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker
