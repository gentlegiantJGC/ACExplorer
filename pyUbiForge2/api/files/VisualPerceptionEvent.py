from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class VisualPerceptionEvent(SubclassBaseFile):
    ResourceType = 0x61CB1693
    ParentResourceType = _Event.ResourceType
    parent: _Event

