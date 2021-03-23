from pyUbiForge2.api.game import SubclassBaseFile
from .SoundEmitterComponent import SoundEmitterComponent as _SoundEmitterComponent


class Ambient3dSoundComponent(SubclassBaseFile):
    ResourceType = 0x99310F0C
    ParentResourceType = _SoundEmitterComponent.ResourceType
    parent: _SoundEmitterComponent
