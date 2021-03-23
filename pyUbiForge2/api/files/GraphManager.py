from pyUbiForge2.api.game import SubclassBaseFile
from .UniverseComponent import UniverseComponent as _UniverseComponent


class GraphManager(SubclassBaseFile):
    ResourceType = 0xFC1DA7EC
    ParentResourceType = _UniverseComponent.ResourceType
    parent: _UniverseComponent
