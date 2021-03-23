from pyUbiForge2.api.game import SubclassBaseFile
from .ITargetEntity import ITargetEntity as _ITargetEntity


class AC2CameraReachHighPointTargetEntity(SubclassBaseFile):
    ResourceType = 0x96EDFE27
    ParentResourceType = _ITargetEntity.ResourceType
    parent: _ITargetEntity

