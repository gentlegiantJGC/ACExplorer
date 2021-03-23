from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class PlayerProgressionManagerDLCElement(SubclassBaseFile):
    ResourceType = 0x9B65777A
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

