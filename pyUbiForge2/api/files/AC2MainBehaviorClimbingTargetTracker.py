from pyUbiForge2.api.game import SubclassBaseFile
from .AC2MainCharacterTargetTracker import (
    AC2MainCharacterTargetTracker as _AC2MainCharacterTargetTracker,
)


class AC2MainBehaviorClimbingTargetTracker(SubclassBaseFile):
    ResourceType = 0x308805E7
    ParentResourceType = _AC2MainCharacterTargetTracker.ResourceType
    parent: _AC2MainCharacterTargetTracker
