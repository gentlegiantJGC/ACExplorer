from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class LargeMeshComponent(SubclassBaseFile):
    ResourceType = 0x7E0DCA4C
    ParentResourceType = _Component.ResourceType
    parent: _Component

