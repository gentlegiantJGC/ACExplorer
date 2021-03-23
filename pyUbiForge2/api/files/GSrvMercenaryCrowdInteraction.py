from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GSrvMercenaryCrowdInteraction(SubclassBaseFile):
    ResourceType = 0x39C52427
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

