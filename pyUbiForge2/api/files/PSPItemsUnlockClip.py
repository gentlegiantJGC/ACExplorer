from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class PSPItemsUnlockClip(SubclassBaseFile):
    ResourceType = 0xD2B82D66
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

