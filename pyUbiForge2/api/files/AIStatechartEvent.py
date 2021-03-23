from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class AIStatechartEvent(SubclassBaseFile):
    ResourceType = 0x4FA4F690
    ParentResourceType = _Event.ResourceType
    parent: _Event

