from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GcLSrvZoneCondition(SubclassBaseFile):
    ResourceType = 0xC09A97A9
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

