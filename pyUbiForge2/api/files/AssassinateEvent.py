from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class AssassinateEvent(SubclassBaseFile):
    ResourceType = 0x86A0B893
    ParentResourceType = _Event.ResourceType
    parent: _Event

