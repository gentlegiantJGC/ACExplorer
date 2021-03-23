from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GliderControlEvent(SubclassBaseFile):
    ResourceType = 0x12AB17DE
    ParentResourceType = _Event.ResourceType
    parent: _Event
