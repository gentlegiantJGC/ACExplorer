from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class CLConflictRuleAlly(SubclassBaseFile):
    ResourceType = 0x93030C2C
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

