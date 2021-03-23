from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class WhiteRoomDLCElement(SubclassBaseFile):
    ResourceType = 0x634F267E
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

