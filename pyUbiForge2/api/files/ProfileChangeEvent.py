from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class ProfileChangeEvent(SubclassBaseFile):
    ResourceType = 0xBB67ECC1
    ParentResourceType = _Event.ResourceType
    parent: _Event

