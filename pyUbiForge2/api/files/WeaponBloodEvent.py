from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class WeaponBloodEvent(SubclassBaseFile):
    ResourceType = 0xF8516872
    ParentResourceType = _Event.ResourceType
    parent: _Event
