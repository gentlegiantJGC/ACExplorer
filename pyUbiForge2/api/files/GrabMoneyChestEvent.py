from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GrabMoneyChestEvent(SubclassBaseFile):
    ResourceType = 0x0D54905F
    ParentResourceType = _Event.ResourceType
    parent: _Event

