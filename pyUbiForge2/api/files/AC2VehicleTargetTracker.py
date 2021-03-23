from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetTracker import ITargetTracker as _ITargetTracker


class AC2VehicleTargetTracker(SubclassBaseFile):
    ResourceType = 0xF1C471C0
    ParentResourceType = _ITargetTracker.ResourceType
    parent: _ITargetTracker

