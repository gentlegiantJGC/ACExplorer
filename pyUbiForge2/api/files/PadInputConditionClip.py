from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class PadInputConditionClip(SubclassBaseFile):
    ResourceType = 0xEA9A4C0B
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

