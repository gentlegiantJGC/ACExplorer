from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GcLSrvShutdown(SubclassBaseFile):
    ResourceType = 0xEA305F35
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
