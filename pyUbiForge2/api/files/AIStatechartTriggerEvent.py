from pyUbiForge2.api.game import SubclassBaseFile
from .AIStatechartEvent import AIStatechartEvent as _AIStatechartEvent


class AIStatechartTriggerEvent(SubclassBaseFile):
    ResourceType = 0x37598D41
    ParentResourceType = _AIStatechartEvent.ResourceType
    parent: _AIStatechartEvent

