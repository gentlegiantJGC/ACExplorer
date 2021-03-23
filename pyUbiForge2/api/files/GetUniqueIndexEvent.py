from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GetUniqueIndexEvent(SubclassBaseFile):
    ResourceType = 0xAC605958
    ParentResourceType = _Event.ResourceType
    parent: _Event
