from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class PuzzleElementActionsComponent_LGS(SubclassBaseFile):
    ResourceType = 0x16BFE5F7
    ParentResourceType = _Component.ResourceType
    parent: _Component
