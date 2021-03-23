from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class LoadOnDemandeDLCElement(SubclassBaseFile):
    ResourceType = 0xA3ADFCAC
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement
