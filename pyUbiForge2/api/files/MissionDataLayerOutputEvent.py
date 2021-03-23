from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionDataLayerOutputEvent(SubclassBaseFile):
    ResourceType = 0xFDF729BF
    ParentResourceType = _Event.ResourceType
    parent: _Event
