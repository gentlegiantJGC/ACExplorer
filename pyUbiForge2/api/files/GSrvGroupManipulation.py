from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GSrvGroupManipulation(SubclassBaseFile):
    ResourceType = 0xA84F908F
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
