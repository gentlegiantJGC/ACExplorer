from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryUniverseComponent import MandatoryUniverseComponent as _MandatoryUniverseComponent


class EconomicSystemSettings(SubclassBaseFile):
    ResourceType = 0xC2F2E93E
    ParentResourceType = _MandatoryUniverseComponent.ResourceType
    parent: _MandatoryUniverseComponent

