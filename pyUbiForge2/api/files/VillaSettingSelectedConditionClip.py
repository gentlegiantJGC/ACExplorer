from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class VillaSettingSelectedConditionClip(SubclassBaseFile):
    ResourceType = 0x5C821031
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
