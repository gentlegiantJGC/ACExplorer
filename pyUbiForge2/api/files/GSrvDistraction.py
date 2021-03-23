from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GSrvDistraction(SubclassBaseFile):
    ResourceType = 0xEB32BD83
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

