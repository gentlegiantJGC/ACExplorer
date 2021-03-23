from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class EntityAIProcess(SubclassBaseFile):
    ResourceType = 0xC90FE3E6
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart
