from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class ShowLogoEvent(SubclassBaseFile):
    ResourceType = 0xF840A48A
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

