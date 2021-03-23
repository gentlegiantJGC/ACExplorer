from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class GoToTitleScreenEvent(SubclassBaseFile):
    ResourceType = 0x6C2B02DF
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
