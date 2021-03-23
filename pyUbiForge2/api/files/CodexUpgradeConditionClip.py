from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class CodexUpgradeConditionClip(SubclassBaseFile):
    ResourceType = 0x8D2B304A
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

