from pyUbiForge2.api.game import SubclassBaseFile
from .ActionAFSMessage import ActionAFSMessage as _ActionAFSMessage


class VillaIncomeChestContentAFSMessage(SubclassBaseFile):
    ResourceType = 0x33A2CC12
    ParentResourceType = _ActionAFSMessage.ResourceType
    parent: _ActionAFSMessage
