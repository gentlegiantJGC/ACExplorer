from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class StrongholdValueChangedEvent(SubclassBaseFile):
    ResourceType = 0x72981C28
    ParentResourceType = _Event.ResourceType
    parent: _Event
