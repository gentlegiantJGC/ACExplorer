from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GliderKickedEvent(SubclassBaseFile):
    ResourceType = 0x169ADEF8
    ParentResourceType = _Event.ResourceType
    parent: _Event
