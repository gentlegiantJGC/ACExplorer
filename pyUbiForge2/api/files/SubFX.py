from pyUbiForge2.api.game import SubclassBaseFile
from .FXElement import FXElement as _FXElement


class SubFX(SubclassBaseFile):
    ResourceType = 0x6DB03CA3
    ParentResourceType = _FXElement.ResourceType
    parent: _FXElement
