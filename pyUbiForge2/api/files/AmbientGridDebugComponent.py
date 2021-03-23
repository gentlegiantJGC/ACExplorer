from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class AmbientGridDebugComponent(SubclassBaseFile):
    ResourceType = 0x83A5B9ED
    ParentResourceType = _Component.ResourceType
    parent: _Component

