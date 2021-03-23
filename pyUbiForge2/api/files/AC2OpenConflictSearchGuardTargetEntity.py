from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetEntity import ITargetEntity as _ITargetEntity


class AC2OpenConflictSearchGuardTargetEntity(SubclassBaseFile):
    ResourceType = 0xD71BC199
    ParentResourceType = _ITargetEntity.ResourceType
    parent: _ITargetEntity
