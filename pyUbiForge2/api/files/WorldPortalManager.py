from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryUniverseComponent import MandatoryUniverseComponent as _MandatoryUniverseComponent


class WorldPortalManager(SubclassBaseFile):
    ResourceType = 0x03091E55
    ParentResourceType = _MandatoryUniverseComponent.ResourceType
    parent: _MandatoryUniverseComponent

