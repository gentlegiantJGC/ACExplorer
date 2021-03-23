from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryUniverseComponent import (
    MandatoryUniverseComponent as _MandatoryUniverseComponent,
)


class MissionManager(SubclassBaseFile):
    ResourceType = 0x59365930
    ParentResourceType = _MandatoryUniverseComponent.ResourceType
    parent: _MandatoryUniverseComponent
