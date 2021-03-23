from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class TestStatechartMoldedBaseClass(SubclassBaseFile):
    ResourceType = 0x6D3F6C69
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
