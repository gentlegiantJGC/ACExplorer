from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class AbstractEntityAI(SubclassBaseFile):
    ResourceType = 0x43986147
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

