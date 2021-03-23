from pyUbiForge2.api.game import SubclassBaseFile
from .ActionAFSMessage import ActionAFSMessage as _ActionAFSMessage


class VillaActionContextualAFSMessage(SubclassBaseFile):
    ResourceType = 0xC46AC24E
    ParentResourceType = _ActionAFSMessage.ResourceType
    parent: _ActionAFSMessage
