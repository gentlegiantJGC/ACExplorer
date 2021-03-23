from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class TimedSwitchComponent_LGS(SubclassBaseFile):
    ResourceType = 0x2151F1B2
    ParentResourceType = _Component.ResourceType
    parent: _Component

