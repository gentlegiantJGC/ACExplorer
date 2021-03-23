from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class WorldDLCElement(SubclassBaseFile):
    ResourceType = 0x148BF4F0
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

