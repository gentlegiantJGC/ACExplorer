from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GcLSrvPatrolTracker(SubclassBaseFile):
    ResourceType = 0xB9DD0DCD
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
