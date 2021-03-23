from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class SetQuickslotEvent(SubclassBaseFile):
    ResourceType = 0xC825EE34
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

