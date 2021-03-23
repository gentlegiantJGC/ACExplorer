from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class DistractedConditionClip(SubclassBaseFile):
    ResourceType = 0x375E5031
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

