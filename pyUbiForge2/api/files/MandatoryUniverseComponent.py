from pyUbiForge2.api.game import SubclassBaseFile
from .UniverseComponent import UniverseComponent as _UniverseComponent


class MandatoryUniverseComponent(SubclassBaseFile):
    ResourceType = 0xC62E24DD
    ParentResourceType = _UniverseComponent.ResourceType
    parent: _UniverseComponent

