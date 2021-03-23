from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class MissionStateTimerUIEvent(SubclassBaseFile):
    ResourceType = 0x079DE661
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

