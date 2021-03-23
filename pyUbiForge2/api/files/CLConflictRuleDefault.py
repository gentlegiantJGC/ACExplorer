from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class CLConflictRuleDefault(SubclassBaseFile):
    ResourceType = 0x9D9A5A38
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
