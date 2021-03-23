from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class SetEntityBuilderClip(SubclassBaseFile):
    ResourceType = 0x5EEE5435
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

