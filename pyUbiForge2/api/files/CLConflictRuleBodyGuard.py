from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class CLConflictRuleBodyGuard(SubclassBaseFile):
    ResourceType = 0xFCF353B4
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

