from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class SoundNotifyConditionClip(SubclassBaseFile):
    ResourceType = 0x0870DCE2
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

