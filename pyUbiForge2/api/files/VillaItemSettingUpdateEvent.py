from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class VillaItemSettingUpdateEvent(SubclassBaseFile):
    ResourceType = 0xECE2261B
    ParentResourceType = _Event.ResourceType
    parent: _Event
