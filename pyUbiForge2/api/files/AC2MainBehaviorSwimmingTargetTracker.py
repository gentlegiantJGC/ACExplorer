from pyUbiForge2.api.game import SubclassBaseFile
from .AC2MainCharacterTargetTracker import AC2MainCharacterTargetTracker as _AC2MainCharacterTargetTracker


class AC2MainBehaviorSwimmingTargetTracker(SubclassBaseFile):
    ResourceType = 0x6F5A1483
    ParentResourceType = _AC2MainCharacterTargetTracker.ResourceType
    parent: _AC2MainCharacterTargetTracker

