from pyUbiForge2.api.game import SubclassBaseFile
from .EventListener import EventListener as _EventListener


class SoundAmbienceManager(SubclassBaseFile):
    ResourceType = 0x87BCF286
    ParentResourceType = _EventListener.ResourceType
    parent: _EventListener
