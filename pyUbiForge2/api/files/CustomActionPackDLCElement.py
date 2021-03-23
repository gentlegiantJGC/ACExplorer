from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class CustomActionPackDLCElement(SubclassBaseFile):
    ResourceType = 0xAB9D5E69
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement
