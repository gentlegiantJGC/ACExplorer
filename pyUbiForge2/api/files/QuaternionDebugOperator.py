from pyUbiForge2.api.game import SubclassBaseFile
from .DebugOperator import DebugOperator as _DebugOperator


class QuaternionDebugOperator(SubclassBaseFile):
    ResourceType = 0x8844E937
    ParentResourceType = _DebugOperator.ResourceType
    parent: _DebugOperator
