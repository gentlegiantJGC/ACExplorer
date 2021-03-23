from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class CodexStateConditionClip(SubclassBaseFile):
    ResourceType = 0x54BBA178
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
