from pyUbiForge2.api.game import SubclassBaseFile
from .SoundLogicEvent import SoundLogicEvent as _SoundLogicEvent


class EnterMainMenuSoundEvent(SubclassBaseFile):
    ResourceType = 0x4B9554C5
    ParentResourceType = _SoundLogicEvent.ResourceType
    parent: _SoundLogicEvent
