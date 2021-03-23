from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GSrvCivilianCrowdInteraction(SubclassBaseFile):
    ResourceType = 0xFEA9FC31
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
