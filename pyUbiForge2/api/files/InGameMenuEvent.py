from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class InGameMenuEvent(SubclassBaseFile):
    ResourceType = 0xF8662538
    ParentResourceType = _Event.ResourceType
    parent: _Event

