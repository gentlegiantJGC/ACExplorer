from pyUbiForge2.api.game import SubclassBaseFile
from .ActionAFSMessage import ActionAFSMessage as _ActionAFSMessage


class FamilyTreeActionAFSMessage(SubclassBaseFile):
    ResourceType = 0xB005419C
    ParentResourceType = _ActionAFSMessage.ResourceType
    parent: _ActionAFSMessage

