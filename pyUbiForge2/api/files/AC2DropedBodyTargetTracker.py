from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2DropedBodyTargetTracker(SubclassBaseFile):
    ResourceType = 0x5E514C91
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker
