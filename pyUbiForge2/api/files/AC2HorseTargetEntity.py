from pyUbiForge2.api.game import SubclassBaseFile
from .MainBehaviorTargetEntity import MainBehaviorTargetEntity as _MainBehaviorTargetEntity


class AC2HorseTargetEntity(SubclassBaseFile):
    ResourceType = 0xBC239A97
    ParentResourceType = _MainBehaviorTargetEntity.ResourceType
    parent: _MainBehaviorTargetEntity

