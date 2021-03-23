from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class FXComponent(SubclassBaseFile):
    ResourceType = 0xD2BF93A6
    ParentResourceType = _Component.ResourceType
    parent: _Component
