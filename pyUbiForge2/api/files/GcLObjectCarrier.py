from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLObjectCarrier(SubclassBaseFile):
    ResourceType = 0x840E8EE8
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

