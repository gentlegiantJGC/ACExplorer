from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class MissionGamePlayPupetteerEvent(SubclassBaseFile):
    ResourceType = 0xE5DFFD44
    ParentResourceType = _Event.ResourceType
    parent: _Event
