from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLSocialize(SubclassBaseFile):
    ResourceType = 0xDF83AA0B
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

