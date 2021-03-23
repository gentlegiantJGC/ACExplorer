from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class QuestItemClip(SubclassBaseFile):
    ResourceType = 0xCD0BAC04
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
