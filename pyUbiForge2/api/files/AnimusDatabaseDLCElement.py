from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class AnimusDatabaseDLCElement(SubclassBaseFile):
    ResourceType = 0x94F799C3
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

