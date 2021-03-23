from pyUbiForge2.api.game import SubclassBaseFile
from .SoundLogicEvent import SoundLogicEvent as _SoundLogicEvent


class EnterLoadingRoomSoundEvent(SubclassBaseFile):
    ResourceType = 0x00260142
    ParentResourceType = _SoundLogicEvent.ResourceType
    parent: _SoundLogicEvent
