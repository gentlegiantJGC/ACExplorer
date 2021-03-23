from pyUbiForge2.api.game import SubclassBaseFile
from .DebugOperator import DebugOperator as _DebugOperator


class IntegerDebugOperator(SubclassBaseFile):
    ResourceType = 0x60062CA8
    ParentResourceType = _DebugOperator.ResourceType
    parent: _DebugOperator

