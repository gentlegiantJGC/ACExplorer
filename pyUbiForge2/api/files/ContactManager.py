from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class ContactManager(SubclassBaseFile):
    ResourceType = 0x915CB4FF
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener

