from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLNPCFollowPlayer(SubclassBaseFile):
    ResourceType = 0xF6D2ADE3
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

