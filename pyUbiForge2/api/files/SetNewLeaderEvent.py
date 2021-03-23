from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class SetNewLeaderEvent(SubclassBaseFile):
    ResourceType = 0x817A7825
    ParentResourceType = _Event.ResourceType
    parent: _Event

