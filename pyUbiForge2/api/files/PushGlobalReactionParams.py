from pyUbiForge2.api.game import SubclassBaseFile
from .PushStateChartParams import PushStateChartParams as _PushStateChartParams


class PushGlobalReactionParams(SubclassBaseFile):
    ResourceType = 0xC10FFC98
    ParentResourceType = _PushStateChartParams.ResourceType
    parent: _PushStateChartParams
