from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GcLSrvReactionTracker(SubclassBaseFile):
    ResourceType = 0xCA710D57
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
