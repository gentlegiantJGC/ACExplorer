from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class SplinePath(SubclassBaseFile):
    ResourceType = 0x316E4710
    ParentResourceType = _Component.ResourceType
    parent: _Component
