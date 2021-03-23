from pyUbiForge2.api.game import SubclassBaseFile
from .SoundLogicEvent import SoundLogicEvent as _SoundLogicEvent


class PlayVideoSoundEvent(SubclassBaseFile):
    ResourceType = 0xFBB9439A
    ParentResourceType = _SoundLogicEvent.ResourceType
    parent: _SoundLogicEvent
