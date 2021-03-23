from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class QuestItemListClip(SubclassBaseFile):
    ResourceType = 0x88E655FA
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

