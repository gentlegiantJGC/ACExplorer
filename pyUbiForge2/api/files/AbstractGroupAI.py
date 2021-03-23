from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class AbstractGroupAI(SubclassBaseFile):
    ResourceType = 0x0EDB5C6F
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
