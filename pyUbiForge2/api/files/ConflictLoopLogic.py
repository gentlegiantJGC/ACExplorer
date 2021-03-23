from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class ConflictLoopLogic(SubclassBaseFile):
    ResourceType = 0x280740E3
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
