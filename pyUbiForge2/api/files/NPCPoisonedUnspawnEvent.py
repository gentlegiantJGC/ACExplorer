from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class NPCPoisonedUnspawnEvent(SubclassBaseFile):
    ResourceType = 0x0DDC91E8
    ParentResourceType = _Event.ResourceType
    parent: _Event

