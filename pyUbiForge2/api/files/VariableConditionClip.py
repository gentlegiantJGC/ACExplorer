from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class VariableConditionClip(SubclassBaseFile):
    ResourceType = 0xA1D7BCF6
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

