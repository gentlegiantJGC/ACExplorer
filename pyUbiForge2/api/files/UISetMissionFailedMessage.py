from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class UISetMissionFailedMessage(SubclassBaseFile):
    ResourceType = 0x1F8E6956
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

