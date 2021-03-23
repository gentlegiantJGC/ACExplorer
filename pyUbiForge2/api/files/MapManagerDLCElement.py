from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class MapManagerDLCElement(SubclassBaseFile):
    ResourceType = 0xE17F5C13
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

