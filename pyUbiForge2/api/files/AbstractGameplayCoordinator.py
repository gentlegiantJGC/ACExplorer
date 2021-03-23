from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class AbstractGameplayCoordinator(SubclassBaseFile):
    ResourceType = 0x185FE1D5
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener
