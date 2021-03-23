from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class SoundManager(SubclassBaseFile):
    ResourceType = 0x8B89559D
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener
