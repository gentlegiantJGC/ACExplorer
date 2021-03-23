from pyUbiForge2.api.game import SubclassBaseFile
from .PlayerInputPickpocketEvent import PlayerInputPickpocketEvent as _PlayerInputPickpocketEvent


class PlayerInputPickpocketActivatedEvent(SubclassBaseFile):
    ResourceType = 0xD0A1C0D3
    ParentResourceType = _PlayerInputPickpocketEvent.ResourceType
    parent: _PlayerInputPickpocketEvent

