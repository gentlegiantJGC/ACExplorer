from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GSrvGroupPolygon(SubclassBaseFile):
    ResourceType = 0xF080256A
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
