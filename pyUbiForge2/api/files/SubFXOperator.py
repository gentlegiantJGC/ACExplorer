from pyUbiForge2.api.game import SubclassBaseFile
from .FXElementOperator import FXElementOperator as _FXElementOperator


class SubFXOperator(SubclassBaseFile):
    ResourceType = 0x1EB94A17
    ParentResourceType = _FXElementOperator.ResourceType
    parent: _FXElementOperator
