from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetEntity import ITargetEntity as _ITargetEntity


class SpawnedTargetEntity(SubclassBaseFile):
    ResourceType = 0x0D2AFCCE
    ParentResourceType = _ITargetEntity.ResourceType
    parent: _ITargetEntity
