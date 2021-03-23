from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryUniverseComponent import MandatoryUniverseComponent as _MandatoryUniverseComponent


class GameStatsManager(SubclassBaseFile):
    ResourceType = 0xF05C4CDC
    ParentResourceType = _MandatoryUniverseComponent.ResourceType
    parent: _MandatoryUniverseComponent

