from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PlayerHealthChangeEvent(SubclassBaseFile):
    ResourceType = 0x5B2ADE22
    ParentResourceType = _Event.ResourceType
    parent: _Event
