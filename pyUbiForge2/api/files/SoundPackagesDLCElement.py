from pyUbiForge2.api.game import SubclassBaseFile
from .ContentElement import ContentElement as _ContentElement


class SoundPackagesDLCElement(SubclassBaseFile):
    ResourceType = 0xCD7927F7
    ParentResourceType = _ContentElement.ResourceType
    parent: _ContentElement

