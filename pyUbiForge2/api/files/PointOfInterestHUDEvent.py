from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class PointOfInterestHUDEvent(SubclassBaseFile):
    ResourceType = 0xC8AE2F63
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
