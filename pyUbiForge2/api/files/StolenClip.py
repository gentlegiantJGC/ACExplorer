from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class StolenClip(SubclassBaseFile):
    ResourceType = 0x0B5660E2
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

