from pyUbiForge2.api.game import SubclassBaseFile
from .PushStateChartParams import PushStateChartParams as _PushStateChartParams


class PushExclusiveReactionParams(SubclassBaseFile):
    ResourceType = 0x4F4D2620
    ParentResourceType = _PushStateChartParams.ResourceType
    parent: _PushStateChartParams
