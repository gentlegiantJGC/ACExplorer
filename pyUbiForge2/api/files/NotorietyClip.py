from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class NotorietyClip(SubclassBaseFile):
    ResourceType = 0xFC96CCC1
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

