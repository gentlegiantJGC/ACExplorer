from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class Clip(SubclassBaseFile):
    ResourceType = 0x0D12BB59
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener

