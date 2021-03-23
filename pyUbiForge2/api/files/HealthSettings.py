from pyUbiForge2.api.game import SubclassBaseFile
from .UniverseComponent import UniverseComponent as _UniverseComponent


class HealthSettings(SubclassBaseFile):
    ResourceType = 0x38B6C671
    ParentResourceType = _UniverseComponent.ResourceType
    parent: _UniverseComponent
