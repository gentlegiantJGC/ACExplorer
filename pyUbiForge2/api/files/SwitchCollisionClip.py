from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SwitchCollisionClip(SubclassBaseFile):
    ResourceType = 0x0EC2C241
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

