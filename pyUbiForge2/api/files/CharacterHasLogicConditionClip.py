from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class CharacterHasLogicConditionClip(SubclassBaseFile):
    ResourceType = 0x76C906A8
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
