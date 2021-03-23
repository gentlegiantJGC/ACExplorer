from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class SkeletonComponent(SubclassBaseFile):
    ResourceType = 0x71FDA747
    ParentResourceType = _Component.ResourceType
    parent: _Component
