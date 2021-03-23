from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class OutOfBoundsEvent(SubclassBaseFile):
    ResourceType = 0xC83A017D
    ParentResourceType = _Event.ResourceType
    parent: _Event

