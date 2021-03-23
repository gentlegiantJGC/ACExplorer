from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class SceneActorStateConditionClip(SubclassBaseFile):
    ResourceType = 0xECA74E09
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
