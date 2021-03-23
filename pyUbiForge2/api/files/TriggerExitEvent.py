from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class TriggerExitEvent(SubclassBaseFile):
    ResourceType = 0xD997BA8E
    ParentResourceType = _Event.ResourceType
    parent: _Event
