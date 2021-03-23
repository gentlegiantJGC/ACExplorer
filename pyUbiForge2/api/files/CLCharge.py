from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class CLCharge(SubclassBaseFile):
    ResourceType = 0xA29E05CB
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

