from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetEntity import ITargetEntity as _ITargetEntity


class PickedTargetEntity(SubclassBaseFile):
    ResourceType = 0xF7E2905B
    ParentResourceType = _ITargetEntity.ResourceType
    parent: _ITargetEntity
