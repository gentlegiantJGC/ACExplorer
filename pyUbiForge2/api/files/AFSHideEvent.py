from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class AFSHideEvent(SubclassBaseFile):
    ResourceType = 0x0DAEED39
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
