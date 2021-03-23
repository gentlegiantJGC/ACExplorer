from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class DLCMaskConditionClip(SubclassBaseFile):
    ResourceType = 0x3032F903
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
