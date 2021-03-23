from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryUniverseComponent import MandatoryUniverseComponent as _MandatoryUniverseComponent


class LoadingScreenComponent(SubclassBaseFile):
    ResourceType = 0x4F2559FF
    ParentResourceType = _MandatoryUniverseComponent.ResourceType
    parent: _MandatoryUniverseComponent

