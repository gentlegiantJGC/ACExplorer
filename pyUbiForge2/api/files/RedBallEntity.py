from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class RedBallEntity(SubclassBaseFile):
    ResourceType = 0x941D0BF8
    ParentResourceType = _Component.ResourceType
    parent: _Component

