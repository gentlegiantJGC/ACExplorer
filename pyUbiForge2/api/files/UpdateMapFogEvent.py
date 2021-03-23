from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class UpdateMapFogEvent(SubclassBaseFile):
    ResourceType = 0xD3F6F33D
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

