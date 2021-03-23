from pyUbiForge2.api.game import SubclassBaseFile
from .GameplayEvent import GameplayEvent as _GameplayEvent


class EavesdroppingExitEvent(SubclassBaseFile):
    ResourceType = 0x2B101589
    ParentResourceType = _GameplayEvent.ResourceType
    parent: _GameplayEvent
