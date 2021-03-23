from pyUbiForge2.api.game import SubclassBaseFile
from .EngineEvent import EngineEvent as _EngineEvent


class EngineLoadWorldEvent(SubclassBaseFile):
    ResourceType = 0x56F6A62D
    ParentResourceType = _EngineEvent.ResourceType
    parent: _EngineEvent
