from pyUbiForge2.api.game import SubclassBaseFile
from .IKGround import IKGround as _IKGround


class IKGroundBiped(SubclassBaseFile):
    ResourceType = 0x346DDDD0
    ParentResourceType = _IKGround.ResourceType
    parent: _IKGround

