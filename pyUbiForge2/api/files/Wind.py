from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class Wind(SubclassBaseFile):
    ResourceType = 0x8139FBC0
    ParentResourceType = _Component.ResourceType
    parent: _Component
