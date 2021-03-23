from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class FreeRunCornerTurnComponent(SubclassBaseFile):
    ResourceType = 0xF8ED7B7B
    ParentResourceType = _Component.ResourceType
    parent: _Component

