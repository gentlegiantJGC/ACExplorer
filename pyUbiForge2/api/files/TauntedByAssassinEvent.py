from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class TauntedByAssassinEvent(SubclassBaseFile):
    ResourceType = 0x6F82842E
    ParentResourceType = _Event.ResourceType
    parent: _Event

