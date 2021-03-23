from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class CLConflictRuleArcher(SubclassBaseFile):
    ResourceType = 0x4D88D979
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

