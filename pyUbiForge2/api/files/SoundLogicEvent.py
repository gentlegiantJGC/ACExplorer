from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class SoundLogicEvent(SubclassBaseFile):
    ResourceType = 0x65BA85CD
    ParentResourceType = _Event.ResourceType
    parent: _Event
