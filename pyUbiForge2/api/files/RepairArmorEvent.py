from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class RepairArmorEvent(SubclassBaseFile):
    ResourceType = 0x1BDE20D0
    ParentResourceType = _Event.ResourceType
    parent: _Event
