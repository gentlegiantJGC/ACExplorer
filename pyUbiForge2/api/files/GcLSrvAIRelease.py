from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GcLSrvAIRelease(SubclassBaseFile):
    ResourceType = 0x74F3484E
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

