from pyUbiForge2.api.game import SubclassBaseFile
from .VictimEvent import VictimEvent as _VictimEvent


class ExitDangerVictimEvent(SubclassBaseFile):
    ResourceType = 0xF4315A4F
    ParentResourceType = _VictimEvent.ResourceType
    parent: _VictimEvent

