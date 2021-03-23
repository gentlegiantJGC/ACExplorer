from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class ReactionHandler(SubclassBaseFile):
    ResourceType = 0x91EF0B3B
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
