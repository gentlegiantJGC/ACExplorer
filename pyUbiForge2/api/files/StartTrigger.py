from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class StartTrigger(SubclassBaseFile):
    ResourceType = 0xFE1B9D2A
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener

