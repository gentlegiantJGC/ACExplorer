from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class NullTargetTracker(SubclassBaseFile):
    ResourceType = 0xFEBCEEA4
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker
