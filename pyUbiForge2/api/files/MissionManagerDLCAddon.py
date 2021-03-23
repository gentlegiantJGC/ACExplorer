from pyUbiForge2.api.game import SubclassBaseFile
from .DLCAddon import DLCAddon as _DLCAddon


class MissionManagerDLCAddon(SubclassBaseFile):
    ResourceType = 0xC0548BC4
    ParentResourceType = _DLCAddon.ResourceType
    parent: _DLCAddon
