from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GcLAbstractGroupManipulationEmbedded(SubclassBaseFile):
    ResourceType = 0xFFCF0FD6
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

