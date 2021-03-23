from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PlayerAdjacencyGroupManipulationEvent(SubclassBaseFile):
    ResourceType = 0xA636C3C6
    ParentResourceType = _Event.ResourceType
    parent: _Event

