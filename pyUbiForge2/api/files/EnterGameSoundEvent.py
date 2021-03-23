from pyUbiForge2.api.game import SubclassBaseFile
from .SoundLogicEvent import SoundLogicEvent as _SoundLogicEvent


class EnterGameSoundEvent(SubclassBaseFile):
    ResourceType = 0x8C95EDC2
    ParentResourceType = _SoundLogicEvent.ResourceType
    parent: _SoundLogicEvent

