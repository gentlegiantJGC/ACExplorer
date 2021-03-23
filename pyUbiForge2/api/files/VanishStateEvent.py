from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class VanishStateEvent(SubclassBaseFile):
    ResourceType = 0x642BED60
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

