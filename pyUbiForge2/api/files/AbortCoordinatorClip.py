from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class AbortCoordinatorClip(SubclassBaseFile):
    ResourceType = 0x01FAC597
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

