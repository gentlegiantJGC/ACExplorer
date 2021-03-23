from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLArcherExotic(SubclassBaseFile):
    ResourceType = 0xA4B3E199
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

