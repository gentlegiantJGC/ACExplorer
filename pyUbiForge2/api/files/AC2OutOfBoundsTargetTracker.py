from pyUbiForge2.api.game import SubclassBaseFile
from .MainBehaviorTargetTracker import (
    MainBehaviorTargetTracker as _MainBehaviorTargetTracker,
)


class AC2OutOfBoundsTargetTracker(SubclassBaseFile):
    ResourceType = 0xB418BE05
    ParentResourceType = _MainBehaviorTargetTracker.ResourceType
    parent: _MainBehaviorTargetTracker
