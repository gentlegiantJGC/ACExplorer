from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class ConstraintComponent(SubclassBaseFile):
    ResourceType = 0xD0345546
    ParentResourceType = _Component.ResourceType
    parent: _Component
