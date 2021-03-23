from pyUbiForge2.api.game import SubclassBaseFile
from .NavFlow import NavFlow as _NavFlow


class CrowdFlow(SubclassBaseFile):
    ResourceType = 0x3BBECB2B
    ParentResourceType = _NavFlow.ResourceType
    parent: _NavFlow
