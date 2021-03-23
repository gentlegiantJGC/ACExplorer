from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class AmbienceEvent(SubclassBaseFile):
    ResourceType = 0xF1670F44
    ParentResourceType = _Event.ResourceType
    parent: _Event
