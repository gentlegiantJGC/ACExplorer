from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class CameraComponent(SubclassBaseFile):
    ResourceType = 0x51C46EA2
    ParentResourceType = _Component.ResourceType
    parent: _Component

