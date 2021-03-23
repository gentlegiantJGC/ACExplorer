from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2AssassinationTargetTracker(SubclassBaseFile):
    ResourceType = 0x441D6851
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker

