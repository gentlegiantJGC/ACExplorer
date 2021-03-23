from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class UniqueEventIDEvent(SubclassBaseFile):
    ResourceType = 0x4FB6E364
    ParentResourceType = _Event.ResourceType
    parent: _Event

