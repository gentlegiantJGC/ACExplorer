from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PlayFacialCustomActionEvent(SubclassBaseFile):
    ResourceType = 0x513BD524
    ParentResourceType = _Event.ResourceType
    parent: _Event
