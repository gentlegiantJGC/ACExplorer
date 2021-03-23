from pyUbiForge2.api.game import SubclassBaseFile
from .WatchActorConditionClip import WatchActorConditionClip as _WatchActorConditionClip


class ActionFilterConditionClip(SubclassBaseFile):
    ResourceType = 0x6925E8FB
    ParentResourceType = _WatchActorConditionClip.ResourceType
    parent: _WatchActorConditionClip
