from pyUbiForge2.api.game import SubclassBaseFile
from .DebugOperator import DebugOperator as _DebugOperator


class FloatDebugOperator(SubclassBaseFile):
    ResourceType = 0x2C5703CC
    ParentResourceType = _DebugOperator.ResourceType
    parent: _DebugOperator

