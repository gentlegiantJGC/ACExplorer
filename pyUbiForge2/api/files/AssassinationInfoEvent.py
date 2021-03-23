from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class AssassinationInfoEvent(SubclassBaseFile):
    ResourceType = 0xED916997
    ParentResourceType = _Event.ResourceType
    parent: _Event

