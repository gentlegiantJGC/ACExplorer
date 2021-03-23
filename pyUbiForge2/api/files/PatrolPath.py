from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class PatrolPath(SubclassBaseFile):
    ResourceType = 0x6D29F95F
    ParentResourceType = _Component.ResourceType
    parent: _Component
