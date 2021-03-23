from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class LocalizationDLCElement(SubclassBaseFile):
    ResourceType = 0x94BE1A97
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

