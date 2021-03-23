from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class CrowdBlobClip(SubclassBaseFile):
    ResourceType = 0x00DC96DD
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

