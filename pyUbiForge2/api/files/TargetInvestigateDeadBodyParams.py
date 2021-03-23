from pyUbiForge2.api.game import SubclassBaseFile
from .InvestigateDeadBodyParams import (
    InvestigateDeadBodyParams as _InvestigateDeadBodyParams,
)


class TargetInvestigateDeadBodyParams(SubclassBaseFile):
    ResourceType = 0x83ECD6D1
    ParentResourceType = _InvestigateDeadBodyParams.ResourceType
    parent: _InvestigateDeadBodyParams
