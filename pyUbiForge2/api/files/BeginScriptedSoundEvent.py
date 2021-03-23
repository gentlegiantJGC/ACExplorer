from pyUbiForge2.api.game import SubclassBaseFile
from .ScriptedSoundEvent import ScriptedSoundEvent as _ScriptedSoundEvent


class BeginScriptedSoundEvent(SubclassBaseFile):
    ResourceType = 0x0248F178
    ParentResourceType = _ScriptedSoundEvent.ResourceType
    parent: _ScriptedSoundEvent

