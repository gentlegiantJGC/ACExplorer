from pyUbiForge2.api.game import SubclassBaseFile
from .UniverseComponent import UniverseComponent as _UniverseComponent


class MenuManager(SubclassBaseFile):
    ResourceType = 0x99712CA9
    ParentResourceType = _UniverseComponent.ResourceType
    parent: _UniverseComponent

