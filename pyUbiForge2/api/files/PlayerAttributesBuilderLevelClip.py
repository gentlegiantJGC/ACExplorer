from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class PlayerAttributesBuilderLevelClip(SubclassBaseFile):
    ResourceType = 0x8BCD0854
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

