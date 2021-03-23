from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class DesynchronizationIgnoreEvent(SubclassBaseFile):
    ResourceType = 0xE7258055
    ParentResourceType = _Event.ResourceType
    parent: _Event

