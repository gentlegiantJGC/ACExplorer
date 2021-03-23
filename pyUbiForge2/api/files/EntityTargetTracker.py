from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class EntityTargetTracker(SubclassBaseFile):
    ResourceType = 0x431EF57C
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker
