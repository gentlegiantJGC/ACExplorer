from pyUbiForge2.api.game import SubclassBaseFile
from .FXElementOperator import FXElementOperator as _FXElementOperator


class FXEngineOperator(SubclassBaseFile):
    ResourceType = 0x04307420
    ParentResourceType = _FXElementOperator.ResourceType
    parent: _FXElementOperator
