from pyUbiForge2.api.game import SubclassBaseFile
from .ScriptedSoundEvent import ScriptedSoundEvent as _ScriptedSoundEvent


class EndScriptedSoundEvent(SubclassBaseFile):
    ResourceType = 0x3FB505E8
    ParentResourceType = _ScriptedSoundEvent.ResourceType
    parent: _ScriptedSoundEvent
