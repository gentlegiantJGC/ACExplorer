from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SetAIDataClip(SubclassBaseFile):
    ResourceType = 0xDED600BF
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

