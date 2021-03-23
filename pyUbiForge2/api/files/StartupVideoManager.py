from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class StartupVideoManager(SubclassBaseFile):
    ResourceType = 0x86508902
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener
