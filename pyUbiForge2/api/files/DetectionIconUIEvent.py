from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class DetectionIconUIEvent(SubclassBaseFile):
    ResourceType = 0x861652C9
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

