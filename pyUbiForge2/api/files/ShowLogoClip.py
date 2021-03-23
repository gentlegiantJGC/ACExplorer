from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ShowLogoClip(SubclassBaseFile):
    ResourceType = 0x4F00989A
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
