from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class UIEvent(SubclassBaseFile):
    ResourceType = 0xF89B9074
    ParentResourceType = _Event.ResourceType
    parent: _Event
