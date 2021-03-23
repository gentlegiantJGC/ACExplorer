from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLShop(SubclassBaseFile):
    ResourceType = 0x22BF60B5
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract

