from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class VillaCodexWallJustOpened(SubclassBaseFile):
    ResourceType = 0xEE4F8C5D
    ParentResourceType = _Event.ResourceType
    parent: _Event

