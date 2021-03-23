from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class ForceAccomplishmentStateClip(SubclassBaseFile):
    ResourceType = 0x2A72C102
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
