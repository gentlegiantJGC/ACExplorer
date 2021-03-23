from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetEntity import ITargetEntity as _ITargetEntity


class AC2DropedBodyTargetEntity(SubclassBaseFile):
    ResourceType = 0x5E4E343B
    ParentResourceType = _ITargetEntity.ResourceType
    parent: _ITargetEntity

