from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class BillboardComponent(SubclassBaseFile):
    ResourceType = 0xF73AA9DF
    ParentResourceType = _Component.ResourceType
    parent: _Component

