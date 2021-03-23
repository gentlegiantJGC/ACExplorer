from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class MaterialOverrider(SubclassBaseFile):
    ResourceType = 0x78A13BF7
    ParentResourceType = _Component.ResourceType
    parent: _Component
