from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class Scene(SubclassBaseFile):
    ResourceType = 0x18B8C0DE
    ParentResourceType = _Component.ResourceType
    parent: _Component
