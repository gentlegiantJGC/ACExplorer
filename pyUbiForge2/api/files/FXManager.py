from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class FXManager(SubclassBaseFile):
    ResourceType = 0x65B7450B
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener
