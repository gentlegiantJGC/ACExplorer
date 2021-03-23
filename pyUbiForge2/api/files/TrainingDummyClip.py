from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class TrainingDummyClip(SubclassBaseFile):
    ResourceType = 0xE05E6A06
    ParentResourceType = _Clip.ResourceType
    parent: _Clip

