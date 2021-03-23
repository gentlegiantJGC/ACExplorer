from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class PlayerSpawnActivatorComponent(SubclassBaseFile):
    ResourceType = 0xA7033693
    ParentResourceType = _Component.ResourceType
    parent: _Component

