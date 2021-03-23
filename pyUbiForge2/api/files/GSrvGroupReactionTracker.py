from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GSrvGroupReactionTracker(SubclassBaseFile):
    ResourceType = 0x22188747
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

