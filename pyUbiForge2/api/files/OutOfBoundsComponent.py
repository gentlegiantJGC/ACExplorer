from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class OutOfBoundsComponent(SubclassBaseFile):
    ResourceType = 0x3DDBFBF3
    ParentResourceType = _Component.ResourceType
    parent: _Component
