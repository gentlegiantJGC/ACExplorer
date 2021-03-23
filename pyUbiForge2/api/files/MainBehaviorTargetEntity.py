from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetEntity import ITargetEntity as _ITargetEntity


class MainBehaviorTargetEntity(SubclassBaseFile):
    ResourceType = 0x3573F547
    ParentResourceType = _ITargetEntity.ResourceType
    parent: _ITargetEntity
