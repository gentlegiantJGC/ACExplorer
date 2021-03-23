from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2CameraReachHighPointTargetTracker(SubclassBaseFile):
    ResourceType = 0x4A98B314
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker

