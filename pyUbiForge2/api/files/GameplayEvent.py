from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GameplayEvent(SubclassBaseFile):
    ResourceType = 0x9AB55ADA
    ParentResourceType = _Event.ResourceType
    parent: _Event

