from pyUbiForge2.api.game import SubclassBaseFile
from .SoundLogicEvent import SoundLogicEvent as _SoundLogicEvent


class ScriptedSoundEvent(SubclassBaseFile):
    ResourceType = 0xD470E95E
    ParentResourceType = _SoundLogicEvent.ResourceType
    parent: _SoundLogicEvent

