from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class RuleGraphClip(SubclassBaseFile):
    ResourceType = 0x403A13ED
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
