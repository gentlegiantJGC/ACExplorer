from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GcLSrvReactionPropagation(SubclassBaseFile):
    ResourceType = 0x9D3069D1
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
