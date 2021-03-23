from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLSiegeTroopWaves(SubclassBaseFile):
    ResourceType = 0xDF8FD2E3
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
