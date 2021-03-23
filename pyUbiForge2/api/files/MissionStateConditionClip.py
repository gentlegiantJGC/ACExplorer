from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class MissionStateConditionClip(SubclassBaseFile):
    ResourceType = 0xB33E6FBF
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

