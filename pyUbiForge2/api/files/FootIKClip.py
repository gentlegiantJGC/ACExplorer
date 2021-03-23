from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class FootIKClip(SubclassBaseFile):
    ResourceType = 0xC93A4172
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
