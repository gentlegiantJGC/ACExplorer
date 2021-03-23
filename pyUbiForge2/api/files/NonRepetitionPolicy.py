from pyUbiForge2.api.game import SubclassBaseFile
from .IExecutionPolicy import IExecutionPolicy as _IExecutionPolicy


class NonRepetitionPolicy(SubclassBaseFile):
    ResourceType = 0x701D1811
    ParentResourceType = _IExecutionPolicy.ResourceType
    parent: _IExecutionPolicy
