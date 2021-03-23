from pyUbiForge2.api.game import SubclassBaseFile
from .UniverseComponent import UniverseComponent as _UniverseComponent


class GroupManipulationSettings(SubclassBaseFile):
    ResourceType = 0x96AE1370
    ParentResourceType = _UniverseComponent.ResourceType
    parent: _UniverseComponent

