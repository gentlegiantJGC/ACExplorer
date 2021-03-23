from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class GuidanceBuilderComponent(SubclassBaseFile):
    ResourceType = 0x742302D6
    ParentResourceType = _Component.ResourceType
    parent: _Component

