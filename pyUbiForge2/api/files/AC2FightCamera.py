from pyUbiForge2.api.game import SubclassBaseFile
from .FightCamera2 import FightCamera2 as _FightCamera2


class AC2FightCamera(SubclassBaseFile):
    ResourceType = 0x480E2F63
    ParentResourceType = _FightCamera2.ResourceType
    parent: _FightCamera2

