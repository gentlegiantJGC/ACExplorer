from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class NextHideSpotToSearchEvent(SubclassBaseFile):
    ResourceType = 0x9B1DC9CD
    ParentResourceType = _Event.ResourceType
    parent: _Event

