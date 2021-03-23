from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class SaveGameComponent(SubclassBaseFile):
    ResourceType = 0x99123179
    ParentResourceType = _Component.ResourceType
    parent: _Component
