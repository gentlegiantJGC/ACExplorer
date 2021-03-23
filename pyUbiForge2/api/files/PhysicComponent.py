from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class PhysicComponent(SubclassBaseFile):
    ResourceType = 0xB4347336
    ParentResourceType = _Component.ResourceType
    parent: _Component

