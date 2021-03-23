from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ProgressStringClip(SubclassBaseFile):
    ResourceType = 0x3B6DF5ED
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

