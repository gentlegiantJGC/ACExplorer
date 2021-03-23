from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class InvestigationIconUIEvent(SubclassBaseFile):
    ResourceType = 0x933D0ACD
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
