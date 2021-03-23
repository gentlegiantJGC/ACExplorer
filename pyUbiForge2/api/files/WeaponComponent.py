from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class WeaponComponent(SubclassBaseFile):
    ResourceType = 0x1C1EEAC3
    ParentResourceType = _Component.ResourceType
    parent: _Component

