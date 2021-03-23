from pyUbiForge2.api.game import SubclassBaseFile
from .GameplayEvent import GameplayEvent as _GameplayEvent


class EavesdroppingEnterEvent(SubclassBaseFile):
    ResourceType = 0xE9C2E14A
    ParentResourceType = _GameplayEvent.ResourceType
    parent: _GameplayEvent
