from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLAmbushWagon(SubclassBaseFile):
    ResourceType = 0xE31C3580
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
