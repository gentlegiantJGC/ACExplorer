from pyUbiForge2.api.game import SubclassBaseFile
from .ConditionClip import ConditionClip as _ConditionClip


class WatchActorConditionClip(SubclassBaseFile):
    ResourceType = 0x5B81D02C
    ParentResourceType = _ConditionClip.ResourceType
    parent: _ConditionClip

