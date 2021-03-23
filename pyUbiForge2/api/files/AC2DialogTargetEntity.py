from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetEntity import ITargetEntity as _ITargetEntity


class AC2DialogTargetEntity(SubclassBaseFile):
    ResourceType = 0x37B2E5F3
    ParentResourceType = _ITargetEntity.ResourceType
    parent: _ITargetEntity

