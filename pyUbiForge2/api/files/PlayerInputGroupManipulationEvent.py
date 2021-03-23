from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PlayerInputGroupManipulationEvent(SubclassBaseFile):
    ResourceType = 0x5F004615
    ParentResourceType = _Event.ResourceType
    parent: _Event

