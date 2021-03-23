from pyUbiForge2.api.game import SubclassBaseFile
from .IExecutionPolicy import IExecutionPolicy as _IExecutionPolicy


class RandomPolicy(SubclassBaseFile):
    ResourceType = 0x51D791DE
    ParentResourceType = _IExecutionPolicy.ResourceType
    parent: _IExecutionPolicy
