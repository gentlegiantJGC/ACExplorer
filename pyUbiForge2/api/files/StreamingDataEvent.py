from pyUbiForge2.api.game import SubclassBaseFile
from .ArrowEvent import ArrowEvent as _ArrowEvent


class StreamingDataEvent(SubclassBaseFile):
    ResourceType = 0x83E2927F
    ParentResourceType = _ArrowEvent.ResourceType
    parent: _ArrowEvent

