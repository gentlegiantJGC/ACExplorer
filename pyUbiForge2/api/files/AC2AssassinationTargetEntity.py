from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetEntity import ITargetEntity as _ITargetEntity


class AC2AssassinationTargetEntity(SubclassBaseFile):
    ResourceType = 0xC8BE892F
    ParentResourceType = _ITargetEntity.ResourceType
    parent: _ITargetEntity

