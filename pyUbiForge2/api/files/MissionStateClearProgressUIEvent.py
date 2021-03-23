from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class MissionStateClearProgressUIEvent(SubclassBaseFile):
    ResourceType = 0xC40BEFBE
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

