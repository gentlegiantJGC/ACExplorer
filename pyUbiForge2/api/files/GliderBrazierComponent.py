from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class GliderBrazierComponent(SubclassBaseFile):
    ResourceType = 0x68C676F2
    ParentResourceType = _Component.ResourceType
    parent: _Component
