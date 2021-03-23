from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLPlayerChaseNPC(SubclassBaseFile):
    ResourceType = 0x06FEA849
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
