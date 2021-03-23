from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class MapManager(SubclassBaseFile):
    ResourceType = 0xC773234A
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
