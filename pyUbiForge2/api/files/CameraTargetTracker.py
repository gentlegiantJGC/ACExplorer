from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class CameraTargetTracker(SubclassBaseFile):
    ResourceType = 0x8E6962C7
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker
