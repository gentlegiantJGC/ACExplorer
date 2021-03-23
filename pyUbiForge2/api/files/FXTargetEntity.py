from pyUbiForge2.api.game import SubclassBaseFile
from .FXElement import FXElement as _FXElement


class FXTargetEntity(SubclassBaseFile):
    ResourceType = 0x67BA0AC5
    ParentResourceType = _FXElement.ResourceType
    parent: _FXElement
