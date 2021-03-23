from pyUbiForge2.api.game import SubclassBaseFile
from .ActorContextData import ActorContextData as _ActorContextData


class VocalizationData(SubclassBaseFile):
    ResourceType = 0x224AEAD3
    ParentResourceType = _ActorContextData.ResourceType
    parent: _ActorContextData

