from pyUbiForge2.api.game import SubclassBaseFile
from .CannonControlDoEvent import CannonControlDoEvent as _CannonControlDoEvent


class CannonControlDoOperateEvent(SubclassBaseFile):
    ResourceType = 0x0C8D0FCB
    ParentResourceType = _CannonControlDoEvent.ResourceType
    parent: _CannonControlDoEvent
