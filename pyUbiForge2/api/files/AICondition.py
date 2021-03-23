from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class AICondition(SubclassBaseFile):
    ResourceType = 0xC7C045E7
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener

