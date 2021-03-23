from pyUbiForge2.api.game import SubclassBaseFile
from .FXElement import FXElement as _FXElement


class FXMaterialOverlay(SubclassBaseFile):
    ResourceType = 0xC9822089
    ParentResourceType = _FXElement.ResourceType
    parent: _FXElement
