from pyUbiForge2.api.game import SubclassBaseFile
from .MainBehaviorTargetEntity import MainBehaviorTargetEntity as _MainBehaviorTargetEntity


class AC2VehicleTargetEntity(SubclassBaseFile):
    ResourceType = 0xC1682992
    ParentResourceType = _MainBehaviorTargetEntity.ResourceType
    parent: _MainBehaviorTargetEntity

