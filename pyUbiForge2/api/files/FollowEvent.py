from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FollowEvent(SubclassBaseFile):
    ResourceType = 0x5FA94E03
    ParentResourceType = _Event.ResourceType
    parent: _Event
