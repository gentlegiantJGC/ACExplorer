from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetEntity import ITargetEntity as _ITargetEntity


class AC2GroupManipulationTargetTargetEntity(SubclassBaseFile):
    ResourceType = 0x43BFED6C
    ParentResourceType = _ITargetEntity.ResourceType
    parent: _ITargetEntity
