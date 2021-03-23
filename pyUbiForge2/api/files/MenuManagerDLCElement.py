from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class MenuManagerDLCElement(SubclassBaseFile):
    ResourceType = 0xD3DCB027
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

