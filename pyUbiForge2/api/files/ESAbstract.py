from pyUbiForge2.api.game import SubclassBaseFile
from .EntityAIProcess import EntityAIProcess as _EntityAIProcess


class ESAbstract(SubclassBaseFile):
    ResourceType = 0x39A73BBF
    ParentResourceType = _EntityAIProcess.ResourceType
    parent: _EntityAIProcess

