from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class ScTimer(SubclassBaseFile):
    ResourceType = 0x6C0257A3
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

