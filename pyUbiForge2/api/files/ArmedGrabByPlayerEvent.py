from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ArmedGrabByPlayerEvent(SubclassBaseFile):
    ResourceType = 0xA66B8D40
    ParentResourceType = _Event.ResourceType
    parent: _Event
