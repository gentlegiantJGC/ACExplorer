from pyUbiForge2.api.game import SubclassBaseFile
from .FXElement import FXElement as _FXElement


class FXMainCharacter(SubclassBaseFile):
    ResourceType = 0x71E31236
    ParentResourceType = _FXElement.ResourceType
    parent: _FXElement

