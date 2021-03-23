from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class Camera(SubclassBaseFile):
    ResourceType = 0x3CB0EB33
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener

