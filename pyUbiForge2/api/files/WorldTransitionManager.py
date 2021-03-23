from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class WorldTransitionManager(SubclassBaseFile):
    ResourceType = 0x0187C7B9
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener

