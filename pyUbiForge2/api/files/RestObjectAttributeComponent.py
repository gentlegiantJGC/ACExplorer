from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class RestObjectAttributeComponent(SubclassBaseFile):
    ResourceType = 0x19BC53F5
    ParentResourceType = _Component.ResourceType
    parent: _Component
