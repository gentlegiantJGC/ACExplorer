from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class MissionStateClearConstraintUIEvent(SubclassBaseFile):
    ResourceType = 0xBDDA9025
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
