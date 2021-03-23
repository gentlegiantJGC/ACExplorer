from pyUbiForge2.api.game import SubclassBaseFile
from .Statechart import Statechart as _Statechart


class GcLSrvAbort(SubclassBaseFile):
    ResourceType = 0x16F14526
    ParentResourceType = _Statechart.ResourceType
    parent: _Statechart

