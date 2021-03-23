from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class VillaCodexPageSettingUpdateEvent(SubclassBaseFile):
    ResourceType = 0x051FFCC2
    ParentResourceType = _Event.ResourceType
    parent: _Event

