from pyUbiForge2.api.game import SubclassBaseFile
from .FXElementOperator import FXElementOperator as _FXElementOperator


class FXMainCharacterOperator(SubclassBaseFile):
    ResourceType = 0xC951B299
    ParentResourceType = _FXElementOperator.ResourceType
    parent: _FXElementOperator
