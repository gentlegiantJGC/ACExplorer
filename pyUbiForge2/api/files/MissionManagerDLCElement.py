from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class MissionManagerDLCElement(SubclassBaseFile):
    ResourceType = 0xBB13C1E1
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement
