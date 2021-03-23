from pyUbiForge2.api.game import SubclassBaseFile
from .DamageEvent import DamageEvent as _DamageEvent


class FightDamageEvent(SubclassBaseFile):
    ResourceType = 0x13F3BE59
    ParentResourceType = _DamageEvent.ResourceType
    parent: _DamageEvent

