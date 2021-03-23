from pyUbiForge2.api.game import SubclassBaseFile
from .PlayerInputPickpocketEvent import PlayerInputPickpocketEvent as _PlayerInputPickpocketEvent


class PlayerInputPickpocketDeactivatedEvent(SubclassBaseFile):
    ResourceType = 0xE7229402
    ParentResourceType = _PlayerInputPickpocketEvent.ResourceType
    parent: _PlayerInputPickpocketEvent

