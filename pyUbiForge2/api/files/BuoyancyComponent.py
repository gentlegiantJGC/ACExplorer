from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class BuoyancyComponent(SubclassBaseFile):
    ResourceType = 0x4B4F7506
    ParentResourceType = _Component.ResourceType
    parent: _Component
