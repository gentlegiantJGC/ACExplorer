from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class MissionManagerDLCElement2(SubclassBaseFile):
    ResourceType = 0xCD637F22
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

