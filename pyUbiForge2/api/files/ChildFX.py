from pyUbiForge2.api.game import SubclassBaseFile
from .FXElement import FXElement as _FXElement


class ChildFX(SubclassBaseFile):
    ResourceType = 0x65B73293
    ParentResourceType = _FXElement.ResourceType
    parent: _FXElement
