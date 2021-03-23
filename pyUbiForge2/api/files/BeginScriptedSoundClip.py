from pyUbiForge2.api.game import SubclassBaseFile
from .ScriptedSoundClip import ScriptedSoundClip as _ScriptedSoundClip


class BeginScriptedSoundClip(SubclassBaseFile):
    ResourceType = 0x48680984
    ParentResourceType = _ScriptedSoundClip.ResourceType
    parent: _ScriptedSoundClip

