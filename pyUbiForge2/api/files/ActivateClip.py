from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ActivateClip(SubclassBaseFile):
    ResourceType = 0xBC8ED33D
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
