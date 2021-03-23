from pyUbiForge2.api.game import SubclassBaseFile
from .DebugOperator import DebugOperator as _DebugOperator


class VectorDebugOperator(SubclassBaseFile):
    ResourceType = 0x8ADDC9B8
    ParentResourceType = _DebugOperator.ResourceType
    parent: _DebugOperator

