from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GSrvScold(SubclassBaseFile):
    ResourceType = 0xB7E3419A
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
