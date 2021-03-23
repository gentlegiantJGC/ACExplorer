from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class DamageEvent(SubclassBaseFile):
    ResourceType = 0x67F2E868
    ParentResourceType = _Event.ResourceType
    parent: _Event

