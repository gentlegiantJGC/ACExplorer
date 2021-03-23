from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class GuidanceSystemComponent(SubclassBaseFile):
    ResourceType = 0xEB482613
    ParentResourceType = _Component.ResourceType
    parent: _Component

