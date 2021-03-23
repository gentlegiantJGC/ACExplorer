from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class VillaBuildingSettingUpdateEvent(SubclassBaseFile):
    ResourceType = 0xC0355209
    ParentResourceType = _Event.ResourceType
    parent: _Event

