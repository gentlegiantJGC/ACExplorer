from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class SelectedWeaponConditionClip(SubclassBaseFile):
    ResourceType = 0xAE30FB9D
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

