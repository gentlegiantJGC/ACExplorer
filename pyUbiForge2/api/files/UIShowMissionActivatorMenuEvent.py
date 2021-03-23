from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class UIShowMissionActivatorMenuEvent(SubclassBaseFile):
    ResourceType = 0x96B0A802
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

