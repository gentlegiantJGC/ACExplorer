from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class StatechartComponent(SubclassBaseFile):
    ResourceType = 0x0828393D
    ParentResourceType = _Component.ResourceType
    parent: _Component

