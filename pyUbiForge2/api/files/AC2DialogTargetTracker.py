from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2DialogTargetTracker(SubclassBaseFile):
    ResourceType = 0xCB87FAC2
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker
