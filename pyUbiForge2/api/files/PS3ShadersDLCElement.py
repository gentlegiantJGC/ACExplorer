from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class PS3ShadersDLCElement(SubclassBaseFile):
    ResourceType = 0x24E6BB4B
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

