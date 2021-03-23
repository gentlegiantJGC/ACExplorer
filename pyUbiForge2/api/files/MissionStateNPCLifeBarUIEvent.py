from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class MissionStateNPCLifeBarUIEvent(SubclassBaseFile):
    ResourceType = 0xEA457D01
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
