from pyUbiForge2.api.game import SubclassBaseFile
from .IKGround import IKGround as _IKGround


class IKGroundQuadruped(SubclassBaseFile):
    ResourceType = 0x72EF5FC9
    ParentResourceType = _IKGround.ResourceType
    parent: _IKGround

