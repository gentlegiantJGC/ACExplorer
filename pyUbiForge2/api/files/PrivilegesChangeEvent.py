from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class PrivilegesChangeEvent(SubclassBaseFile):
    ResourceType = 0xF4C1D362
    ParentResourceType = _Event.ResourceType
    parent: _Event

