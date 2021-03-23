from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class AnimComponent(SubclassBaseFile):
    ResourceType = 0x8C8AA19D
    ParentResourceType = _Component.ResourceType
    parent: _Component
