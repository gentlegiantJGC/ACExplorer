from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GcLAbstract(SubclassBaseFile):
    ResourceType = 0x7FE3107E
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
