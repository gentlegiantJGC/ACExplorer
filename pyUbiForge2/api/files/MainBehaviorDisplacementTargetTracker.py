from pyUbiForge2.api.game import SubclassBaseFile
from .MainBehaviorTargetTracker import (
    MainBehaviorTargetTracker as _MainBehaviorTargetTracker,
)


class MainBehaviorDisplacementTargetTracker(SubclassBaseFile):
    ResourceType = 0x7AAD0D58
    ParentResourceType = _MainBehaviorTargetTracker.ResourceType
    parent: _MainBehaviorTargetTracker
