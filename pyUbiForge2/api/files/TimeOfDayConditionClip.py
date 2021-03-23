from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class TimeOfDayConditionClip(SubclassBaseFile):
    ResourceType = 0xEADEB281
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
