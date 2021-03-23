from pyUbiForge2.api.game import SubclassBaseFile
from .AbstractAIDataParams import AbstractAIDataParams as _AbstractAIDataParams


class AIDataParams(SubclassBaseFile):
    ResourceType = 0x9D245AFA
    ParentResourceType = _AbstractAIDataParams.ResourceType
    parent: _AbstractAIDataParams

