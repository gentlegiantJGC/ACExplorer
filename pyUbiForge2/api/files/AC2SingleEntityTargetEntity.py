from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetEntity import ITargetEntity as _ITargetEntity


class AC2SingleEntityTargetEntity(SubclassBaseFile):
    ResourceType = 0xEEAE3CCA
    ParentResourceType = _ITargetEntity.ResourceType
    parent: _ITargetEntity
