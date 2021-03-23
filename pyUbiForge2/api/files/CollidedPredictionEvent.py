from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class CollidedPredictionEvent(SubclassBaseFile):
    ResourceType = 0x5B4CA0CC
    ParentResourceType = _Event.ResourceType
    parent: _Event
