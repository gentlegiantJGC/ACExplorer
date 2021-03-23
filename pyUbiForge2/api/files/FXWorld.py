from pyUbiForge2.api.game import SubclassBaseFile
from .FXElement import FXElement as _FXElement


class FXWorld(SubclassBaseFile):
    ResourceType = 0x67FEDCFD
    ParentResourceType = _FXElement.ResourceType
    parent: _FXElement
