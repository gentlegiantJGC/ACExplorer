from pyUbiForge2.api.game import SubclassBaseFile
from .FXElementOperator import FXElementOperator as _FXElementOperator


class FXMaterialOverlayOperator(SubclassBaseFile):
    ResourceType = 0x1A645DC3
    ParentResourceType = _FXElementOperator.ResourceType
    parent: _FXElementOperator

