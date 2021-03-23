from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryUniverseComponent import MandatoryUniverseComponent as _MandatoryUniverseComponent


class SceneActionFilterManager(SubclassBaseFile):
    ResourceType = 0x06C82F95
    ParentResourceType = _MandatoryUniverseComponent.ResourceType
    parent: _MandatoryUniverseComponent

