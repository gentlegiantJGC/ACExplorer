from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryUniverseComponent import (
    MandatoryUniverseComponent as _MandatoryUniverseComponent,
)


class VillaGlobalManager(SubclassBaseFile):
    ResourceType = 0xF851B3F5
    ParentResourceType = _MandatoryUniverseComponent.ResourceType
    parent: _MandatoryUniverseComponent
