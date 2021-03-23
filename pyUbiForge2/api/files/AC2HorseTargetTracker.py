from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2HorseTargetTracker(SubclassBaseFile):
    ResourceType = 0x81D3CEFC
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker
