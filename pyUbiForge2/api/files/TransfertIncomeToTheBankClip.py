from pyUbiForge2.api.game import SubclassBaseFile
from .Clip import Clip as _Clip


class TransfertIncomeToTheBankClip(SubclassBaseFile):
    ResourceType = 0xA9D6C354
    ParentResourceType = _Clip.ResourceType
    parent: _Clip
