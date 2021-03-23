from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GSrvTargeting(SubclassBaseFile):
    ResourceType = 0x5EAE8454
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
