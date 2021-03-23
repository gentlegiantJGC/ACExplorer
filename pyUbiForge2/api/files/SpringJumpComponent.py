from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class SpringJumpComponent(SubclassBaseFile):
    ResourceType = 0x87A7C1AA
    ParentResourceType = _Component.ResourceType
    parent: _Component
