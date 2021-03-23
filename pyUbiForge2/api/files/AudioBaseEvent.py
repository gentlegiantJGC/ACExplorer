from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class AudioBaseEvent(SubclassBaseFile):
    ResourceType = 0xDF260DA5
    ParentResourceType = _Event.ResourceType
    parent: _Event
