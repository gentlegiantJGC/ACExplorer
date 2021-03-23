from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class GliderDamageEvent(SubclassBaseFile):
    ResourceType = 0x93746F1C
    ParentResourceType = _Event.ResourceType
    parent: _Event
