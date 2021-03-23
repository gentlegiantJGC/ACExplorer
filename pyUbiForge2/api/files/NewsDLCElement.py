from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class NewsDLCElement(SubclassBaseFile):
    ResourceType = 0x6423C46E
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

