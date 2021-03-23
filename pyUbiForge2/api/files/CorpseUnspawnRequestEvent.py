from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CorpseUnspawnRequestEvent(SubclassBaseFile):
    ResourceType = 0x2F1035DC
    ParentResourceType = _Event.ResourceType
    parent: _Event
