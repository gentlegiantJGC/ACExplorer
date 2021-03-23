from pyUbiForge2.api.game import SubclassBaseFile
from .MainBehaviorTargetTracker import MainBehaviorTargetTracker as _MainBehaviorTargetTracker


class AC2MainCharacterTargetTracker(SubclassBaseFile):
    ResourceType = 0x585A7386
    ParentResourceType = _MainBehaviorTargetTracker.ResourceType
    parent: _MainBehaviorTargetTracker

