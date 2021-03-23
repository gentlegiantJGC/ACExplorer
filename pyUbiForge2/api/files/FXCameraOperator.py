from pyUbiForge2.api.game import SubclassBaseFile
from .FXElementOperator import FXElementOperator as _FXElementOperator


class FXCameraOperator(SubclassBaseFile):
    ResourceType = 0x5BD1A06F
    ParentResourceType = _FXElementOperator.ResourceType
    parent: _FXElementOperator
