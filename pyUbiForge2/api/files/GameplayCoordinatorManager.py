from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class GameplayCoordinatorManager(SubclassBaseFile):
    ResourceType = 0xBA7843F9
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener
