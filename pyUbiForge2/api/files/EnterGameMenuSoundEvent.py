from pyUbiForge2.api.game import SubclassBaseFile
from .SoundLogicEvent import SoundLogicEvent as _SoundLogicEvent


class EnterGameMenuSoundEvent(SubclassBaseFile):
    ResourceType = 0x53D57B33
    ParentResourceType = _SoundLogicEvent.ResourceType
    parent: _SoundLogicEvent
