from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class AbstractGameplayCoordinatorLogic(SubclassBaseFile):
    ResourceType = 0xDF55BF09
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
