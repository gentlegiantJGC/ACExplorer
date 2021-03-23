from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class TargetChaseEvent(SubclassBaseFile):
    ResourceType = 0xBA1E79E1
    ParentResourceType = _Event.ResourceType
    parent: _Event

