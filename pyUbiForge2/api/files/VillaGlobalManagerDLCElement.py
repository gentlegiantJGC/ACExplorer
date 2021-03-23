from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class VillaGlobalManagerDLCElement(SubclassBaseFile):
    ResourceType = 0xB16F7E09
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement
