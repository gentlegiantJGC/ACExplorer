from pyUbiForge2.api.game import SubclassBaseFile
from .ScriptedSoundClip import ScriptedSoundClip as _ScriptedSoundClip


class EndScriptedSoundClip(SubclassBaseFile):
    ResourceType = 0x6D094EE1
    ParentResourceType = _ScriptedSoundClip.ResourceType
    parent: _ScriptedSoundClip

