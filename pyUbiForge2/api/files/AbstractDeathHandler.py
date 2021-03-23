from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class AbstractDeathHandler(SubclassBaseFile):
    ResourceType = 0x1E168B54
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
