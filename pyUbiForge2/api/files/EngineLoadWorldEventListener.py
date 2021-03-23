from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class EngineLoadWorldEventListener(SubclassBaseFile):
    ResourceType = 0x5E7A07C8
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener
