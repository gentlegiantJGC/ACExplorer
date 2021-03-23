from pyUbiForge2.api.game import SubclassBaseFile
from .SoundLogicEvent import SoundLogicEvent as _SoundLogicEvent


class EnterBlackroomSoundEvent(SubclassBaseFile):
    ResourceType = 0xC3814C07
    ParentResourceType = _SoundLogicEvent.ResourceType
    parent: _SoundLogicEvent

