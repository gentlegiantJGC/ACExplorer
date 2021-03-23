from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FamilyTreeClip(SubclassBaseFile):
    ResourceType = 0x3E3CACDF
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

