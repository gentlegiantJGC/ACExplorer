from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLCivilianSocialize(SubclassBaseFile):
    ResourceType = 0x8BD726E2
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
