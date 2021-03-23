from pyUbiForge2.api.game import SubclassBaseFile
from .ReactionParams import ReactionParams as _ReactionParams


class PushStateChartParams(SubclassBaseFile):
    ResourceType = 0x951B2BBA
    ParentResourceType = _ReactionParams.ResourceType
    parent: _ReactionParams

