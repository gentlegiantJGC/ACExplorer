from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class CoordinatorOutputConditionClip(SubclassBaseFile):
    ResourceType = 0xAFEC17D7
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

