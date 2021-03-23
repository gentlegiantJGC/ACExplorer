from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class GameplayCoordinatorComponent(SubclassBaseFile):
    ResourceType = 0x1D566A63
    ParentResourceType = _Component.ResourceType
    parent: _Component

