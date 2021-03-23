from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PlayerInputPickpocketEvent(SubclassBaseFile):
    ResourceType = 0x79927887
    ParentResourceType = _Event.ResourceType
    parent: _Event
