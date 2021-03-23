from pyUbiForge2.api.game import SubclassBaseFile
from .FXElement import FXElement as _FXElement


class FXCamera(SubclassBaseFile):
    ResourceType = 0x1798F943
    ParentResourceType = _FXElement.ResourceType
    parent: _FXElement

