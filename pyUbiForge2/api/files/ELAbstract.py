from pyUbiForge2.api.game import SubclassBaseFile
from .EntityAIProcess import EntityAIProcess as _EntityAIProcess


class ELAbstract(SubclassBaseFile):
    ResourceType = 0x4ADEB61F
    ParentResourceType = _EntityAIProcess.ResourceType
    parent: _EntityAIProcess
