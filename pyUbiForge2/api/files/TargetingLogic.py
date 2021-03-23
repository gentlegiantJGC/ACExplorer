from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class TargetingLogic(SubclassBaseFile):
    ResourceType = 0xC5E023D9
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

