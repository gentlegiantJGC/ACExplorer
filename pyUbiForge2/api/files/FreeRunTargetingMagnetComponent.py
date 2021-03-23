from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class FreeRunTargetingMagnetComponent(SubclassBaseFile):
    ResourceType = 0x4108D49C
    ParentResourceType = _Component.ResourceType
    parent: _Component
