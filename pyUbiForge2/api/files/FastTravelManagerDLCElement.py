from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class FastTravelManagerDLCElement(SubclassBaseFile):
    ResourceType = 0xC0BD1C74
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

