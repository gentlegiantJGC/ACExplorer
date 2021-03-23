from pyUbiForge2.api.game import SubclassBaseFile
from .FXElementOperator import FXElementOperator as _FXElementOperator


class ChildFXOperator(SubclassBaseFile):
    ResourceType = 0xE63E194E
    ParentResourceType = _FXElementOperator.ResourceType
    parent: _FXElementOperator
