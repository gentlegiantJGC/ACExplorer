from pyUbiForge2.api.game import SubclassBaseFile
from .DLCAddon import DLCAddon as _DLCAddon


class WhiteRoomDLCAddon(SubclassBaseFile):
    ResourceType = 0xD21119F5
    ParentResourceType = _DLCAddon.ResourceType
    parent: _DLCAddon
