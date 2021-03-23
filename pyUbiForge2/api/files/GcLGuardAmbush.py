from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLGuardAmbush(SubclassBaseFile):
    ResourceType = 0x67D07D02
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
