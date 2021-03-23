from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class MissionIntroActivatorComponent(SubclassBaseFile):
    ResourceType = 0x2B894696
    ParentResourceType = _Component.ResourceType
    parent: _Component
