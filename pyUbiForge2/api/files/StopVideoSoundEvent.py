from pyUbiForge2.api.game import SubclassBaseFile
from .SoundLogicEvent import SoundLogicEvent as _SoundLogicEvent


class StopVideoSoundEvent(SubclassBaseFile):
    ResourceType = 0xFD42C16F
    ParentResourceType = _SoundLogicEvent.ResourceType
    parent: _SoundLogicEvent

