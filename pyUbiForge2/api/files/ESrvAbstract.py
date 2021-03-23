from pyUbiForge2.api.game import SubclassBaseFile
from .EntityAIProcess import EntityAIProcess as _EntityAIProcess


class ESrvAbstract(SubclassBaseFile):
    ResourceType = 0xAA2DB0CE
    ParentResourceType = _EntityAIProcess.ResourceType
    parent: _EntityAIProcess
