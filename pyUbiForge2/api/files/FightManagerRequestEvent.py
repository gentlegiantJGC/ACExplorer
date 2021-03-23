from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class FightManagerRequestEvent(SubclassBaseFile):
    ResourceType = 0x40164C2E
    ParentResourceType = _Event.ResourceType
    parent: _Event

