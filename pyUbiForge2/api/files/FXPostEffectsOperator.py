from pyUbiForge2.api.game import SubclassBaseFile
from .FXElementOperator import FXElementOperator as _FXElementOperator


class FXPostEffectsOperator(SubclassBaseFile):
    ResourceType = 0x5F76AEC9
    ParentResourceType = _FXElementOperator.ResourceType
    parent: _FXElementOperator
