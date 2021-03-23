from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryUniverseComponent import (
    MandatoryUniverseComponent as _MandatoryUniverseComponent,
)


class GamePlaySettings(SubclassBaseFile):
    ResourceType = 0x91831427
    ParentResourceType = _MandatoryUniverseComponent.ResourceType
    parent: _MandatoryUniverseComponent
