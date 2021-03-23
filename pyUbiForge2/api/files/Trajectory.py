from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class Trajectory(SubclassBaseFile):
    ResourceType = 0xAB0AECD7
    ParentResourceType = _Component.ResourceType
    parent: _Component
