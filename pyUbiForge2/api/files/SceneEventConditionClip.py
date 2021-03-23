from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class SceneEventConditionClip(SubclassBaseFile):
    ResourceType = 0xC1E82279
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip
