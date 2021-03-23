from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class BreakableShakeEvent(SubclassBaseFile):
    ResourceType = 0x941A68D7
    ParentResourceType = _Event.ResourceType
    parent: _Event

