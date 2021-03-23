from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GCLFightDummyTestTool(SubclassBaseFile):
    ResourceType = 0xFDFB050A
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
