from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class SwitchableTargetTracker(SubclassBaseFile):
    ResourceType = 0x849648F4
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker

