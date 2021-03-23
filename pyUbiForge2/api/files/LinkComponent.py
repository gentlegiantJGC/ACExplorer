from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class LinkComponent(SubclassBaseFile):
    ResourceType = 0x9B1B4DA8
    ParentResourceType = _Component.ResourceType
    parent: _Component
