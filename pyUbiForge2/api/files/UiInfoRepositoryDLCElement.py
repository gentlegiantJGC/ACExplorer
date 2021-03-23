from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class UiInfoRepositoryDLCElement(SubclassBaseFile):
    ResourceType = 0x76EB4A1E
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

