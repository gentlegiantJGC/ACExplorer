from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class ActivationEventListener(SubclassBaseFile):
    ResourceType = 0x143E5904
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener
