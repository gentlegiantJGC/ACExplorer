from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryUniverseComponent import (
    MandatoryUniverseComponent as _MandatoryUniverseComponent,
)


class FireGlobalData(SubclassBaseFile):
    ResourceType = 0x68687467
    ParentResourceType = _MandatoryUniverseComponent.ResourceType
    parent: _MandatoryUniverseComponent
