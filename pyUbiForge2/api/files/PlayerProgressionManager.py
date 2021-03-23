from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryUniverseComponent import (
    MandatoryUniverseComponent as _MandatoryUniverseComponent,
)


class PlayerProgressionManager(SubclassBaseFile):
    ResourceType = 0x9713A15F
    ParentResourceType = _MandatoryUniverseComponent.ResourceType
    parent: _MandatoryUniverseComponent
