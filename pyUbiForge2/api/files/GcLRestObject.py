from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLRestObject(SubclassBaseFile):
    ResourceType = 0xC33A1B0D
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

