from pyUbiForge2.api.game import SubclassBaseFile
from .FXElementOperator import FXElementOperator as _FXElementOperator


class FXTargetEntityOperator(SubclassBaseFile):
    ResourceType = 0x28A54884
    ParentResourceType = _FXElementOperator.ResourceType
    parent: _FXElementOperator

