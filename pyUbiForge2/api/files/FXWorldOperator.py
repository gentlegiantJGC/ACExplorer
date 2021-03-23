from pyUbiForge2.api.game import SubclassBaseFile
from .FXElementOperator import FXElementOperator as _FXElementOperator


class FXWorldOperator(SubclassBaseFile):
    ResourceType = 0x22577E49
    ParentResourceType = _FXElementOperator.ResourceType
    parent: _FXElementOperator
