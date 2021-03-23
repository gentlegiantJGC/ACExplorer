from pyUbiForge2.api.game import SubclassBaseFile
from .PushStateChartParams import PushStateChartParams as _PushStateChartParams


class PushConcurrentReactionParams(SubclassBaseFile):
    ResourceType = 0x6EC67D59
    ParentResourceType = _PushStateChartParams.ResourceType
    parent: _PushStateChartParams

