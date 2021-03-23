from pyUbiForge2.api.game import SubclassBaseFile
from .FXElement import FXElement as _FXElement


class FXEngine(SubclassBaseFile):
    ResourceType = 0xC42C0DCB
    ParentResourceType = _FXElement.ResourceType
    parent: _FXElement
